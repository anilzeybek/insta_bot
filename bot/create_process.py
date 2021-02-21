from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from login_page import LoginPage
from user_page import UserPage
from post_page import PostPage
from hashtag_page import HashtagPage
from dm_page import DmPage
import random
from database_utils import add_blacklist, in_blacklist, find_follow_requests, delete_follow_request, add_user
from datetime import datetime
from time import sleep
import sys
import json
import logging


REMAINING_REQUESTS = 0
REMAINING_LIKES = 0
REMAINING_DM = 0

MIN_TIME = 0
MAX_TIME = 0

logging.basicConfig(filename='../logfile.log', level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options, executable_path="../geckodriver", service_log_path='/dev/null')
browser.implicitly_wait(5)

user_list = []
messages_init = []
messages = []


def like_or_follow_request_or_dm(user_page, post_page, dm_page, target_users):
    global REMAINING_REQUESTS, REMAINING_LIKES, REMAINING_DM

    for user in target_users:
        if not in_blacklist(user) and user not in user_list:
            locked_acc = user_page.go_user(user)

            if not locked_acc and REMAINING_LIKES > 0:
                post_no = random.randint(1, 3)

                user_page.go_post(post_no)
                result = post_page.like_post(user)

                if result:
                    add_blacklist(user)
                    REMAINING_LIKES -= 1

                    logging.warning(f"liked post of {user}")
                    logging.warning(f"remaining likes: {REMAINING_LIKES}")
            elif locked_acc and REMAINING_REQUESTS > 0:
                user_page.send_follow_request(user)

                add_blacklist(user)
                REMAINING_REQUESTS -= 1

                logging.warning(f"follow request sent to {user}")
                logging.warning(f"remaining requests: {REMAINING_REQUESTS}")
            elif locked_acc and REMAINING_DM > 0:
                dm_page.send_message(user, messages.pop(0))

                add_blacklist(user)
                REMAINING_DM -= 1

                logging.warning(f"dm sent to {user}")
                logging.warning(f"remaining dm: {REMAINING_DM}")
            elif REMAINING_LIKES <= 0 and REMAINING_REQUESTS <= 0 and REMAINING_DM <= 0:
                return

            sleep(random.randint(MIN_TIME, MAX_TIME))


def check_user(user_page, post_page, dm_page, look_followers, how_many_followers, keywords, username):
    global REMAINING_REQUESTS, REMAINING_LIKES, REMAINING_DM

    locked_acc = user_page.go_user(username)
    if not locked_acc:
        if look_followers:
            if REMAINING_REQUESTS > 0 or REMAINING_LIKES > 0 or REMAINING_DM > 0:
                logging.warning(f"looking followers of the {username}")

                target_users = user_page.get_followers(how_many_followers)
                like_or_follow_request_or_dm(user_page, post_page, dm_page, target_users)
            else:
                return True

        else:
            for post_no in range(1, 6):
                if REMAINING_REQUESTS > 0 or REMAINING_LIKES > 0 or REMAINING_DM > 0:
                    logging.warning(f"looking at post of target user {username}")
                    user_page.go_post(post_no)
                    target_users = post_page.find_target_users(keywords)

                    like_or_follow_request_or_dm(user_page, post_page, dm_page, target_users)
                    user_page.go_user(username)
                else:
                    return True

    return False


def create_process(login_user, login_password, look_followers, how_many_followers,
                   keywords, daily_request_limit, daily_like_limit, daily_dm_limit):
    global REMAINING_REQUESTS, REMAINING_LIKES, REMAINING_DM, messages, messages_init, user_list

    login_page = LoginPage(browser, login_user, login_password)
    user_page = UserPage(browser, login_user)
    post_page = PostPage(browser, login_user)
    dm_page = DmPage(browser, login_user)

    login_page.login()

    REMAINING_REQUESTS, REMAINING_LIKES, REMAINING_DM = daily_request_limit, daily_like_limit, daily_dm_limit
    reset_time = datetime.now()

    while True:
        if (datetime.now() - reset_time).total_seconds() > 70000:
            logging.warning("Resetting remaining requests, likes and dm")
            reset_time = datetime.now()

            REMAINING_REQUESTS, REMAINING_LIKES, REMAINING_DM = daily_request_limit, daily_like_limit, daily_dm_limit
            random.shuffle(user_list)
            random.shuffle(messages_init)

            messages = messages_init


        for username in user_list:
            try:
                logging.warning(f"going to target user {username}")
                over = check_user(user_page, post_page, dm_page, look_followers,
                                  how_many_followers, keywords, username)
                if over:
                    break
            except Exception as e:
                logging.warning(e)
                sleep(10)

        if REMAINING_REQUESTS == 0 and REMAINING_LIKES == 0 and REMAINING_DM == 0:
            logging.warning("Going into sleep mode since no remaining requests, likes and dm")
            sleep(80000)


def undo_request(login_user, login_password, days):
    login_page = LoginPage(browser, login_user, login_password)
    user_page = UserPage(browser, login_user)

    login_page.login()
    usernames = find_follow_requests(login_user, days)
    logging.warning("undo people: ", usernames)

    for username in usernames:
        try:
            logging.warning(f"unfollowing {username}")

            user_page.go_user(username)
            user_page.undo_follow_request()
            delete_follow_request(login_user, username)

            sleep(random.randint(MIN_TIME, MAX_TIME))
        except Exception as e:
            logging.warning(e)
            sleep(10)


def find_hashtags(login_user, login_password, hashtags):
    login_page = LoginPage(browser, login_user, login_password)
    hashtag_page = HashtagPage(browser)
    post_page = PostPage(browser, login_user)

    login_page.login()
    usernames = set()

    for hashtag in hashtags:
        hashtag_page.go_hashtag(hashtag)
        post_links = hashtag_page.get_post_links()

        for post_link in post_links:
            try:
                post_page.go_post(post_link)

                username = post_page.get_username()
                usernames.add(username)
            except Exception as e:
                logging.warning(e)

    for username in list(set(usernames)):
        add_user(username)


def main():
    global MIN_TIME, MAX_TIME, messages, messages_init, user_list

    filename = sys.argv[1]
    with open(f"../{filename}") as json_file:
        json_content = json.load(json_file)

        login_user = json_content["username"]
        login_password = json_content["password"]

        if "FIND_HASHTAG" in json_content:
            logging.warning("finding hashtags")

            hashtags = json_content["hashtags"].split("\n")
            find_hashtags(login_user, login_password, hashtags)
        elif "UNDO_REQUEST" in json_content:
            logging.warning("undo requests")

            MIN_TIME = json_content["minTime"]
            MAX_TIME = json_content["maxTime"]

            days = json_content["days"]
            undo_request(login_user, login_password, days)
        else:
            logging.warning("creating bot")

            MIN_TIME = json_content["minTime"]
            MAX_TIME = json_content["maxTime"]

            user_list = json_content["targets"].split("\n")
            look_followers = json_content["lookFollowers"]
            how_many_followers = json_content["howManyFollowers"]
            keywords = json_content["keywords"].split("\n")
            messages = json_content["messages"]
            messages_init = json_content["messages"]

            daily_request_limit = json_content["requestLimit"]
            daily_like_limit = json_content["likeLimit"]
            daily_dm_limit = json_content["dmLimit"]

            create_process(login_user, login_password, look_followers, how_many_followers,
                           keywords, daily_request_limit, daily_like_limit, daily_dm_limit)


if __name__ == "__main__":
    main()
