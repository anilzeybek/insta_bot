from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from login_page import LoginPage
from user_page import UserPage
from post_page import PostPage
from dm_page import DmPage
import random
from database_utils import add_blacklist, in_blacklist, find_follow_requests, delete_follow_request
from datetime import datetime
from time import sleep
import sys
import json

REMAINING_REQUESTS = 0
REMAINING_LIKES = 0
REMAINING_DM = 0

MIN_TIME = 0
MAX_TIME = 0

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options, executable_path="../geckodriver")
browser.implicitly_wait(5)

messages_init = []
messages = []


def like_or_follow_request_or_dm(user_page, post_page, dm_page, target_users):
    global REMAINING_REQUESTS, REMAINING_LIKES, REMAINING_DM

    for user in target_users:
        if not in_blacklist(user):
            locked_acc = user_page.go_user(user)

            if not locked_acc and REMAINING_LIKES > 0:
                post_no = random.randint(1, 5)

                user_page.go_post(post_no)
                post_page.like_post(user)

                add_blacklist(user)
                REMAINING_LIKES -= 1

                print(f"remaining likes: {REMAINING_LIKES}")
            elif locked_acc and REMAINING_REQUESTS > 0:
                user_page.send_follow_request(user)

                add_blacklist(user)
                REMAINING_REQUESTS -= 1

                print(f"remaining requests: {REMAINING_REQUESTS}")
            elif locked_acc and REMAINING_DM > 0:
                dm_page.send_message(user, messages.pop(0))

                add_blacklist(user)
                REMAINING_DM -= 1

                print(f"remaining dm: {REMAINING_DM}")
            elif REMAINING_LIKES <= 0 and REMAINING_REQUESTS <= 0 and REMAINING_DM <= 0:
                return

            sleep(random.randint(MIN_TIME, MAX_TIME))


def check_user(user_page, post_page, dm_page, look_followers, keywords, username):
    global REMAINING_REQUESTS, REMAINING_LIKES, REMAINING_DM

    locked_acc = user_page.go_user(username)
    if not locked_acc:
        if look_followers:
            if REMAINING_REQUESTS > 0 or REMAINING_LIKES > 0 or REMAINING_DM > 0:
                print(f"looking followers of the {username}")

                target_users = user_page.get_followers()
                like_or_follow_request_or_dm(user_page, post_page, dm_page, target_users)
            else:
                return True

        else:
            for post_no in range(1, 6):
                if REMAINING_REQUESTS > 0 or REMAINING_LIKES > 0 or REMAINING_DM > 0:
                    user_page.go_post(post_no)
                    target_users = post_page.find_target_users(keywords)

                    like_or_follow_request_or_dm(user_page, post_page, dm_page, target_users)
                    user_page.go_user(username)

                else:
                    return True

    return False


def create_process(login_user, login_password, user_list, look_followers,
                keywords, daily_request_limit, daily_like_limit, daily_dm_limit):
    global REMAINING_REQUESTS, REMAINING_LIKES, REMAINING_DM, messages, messages_init

    login_page = LoginPage(browser, login_user, login_password)
    user_page = UserPage(browser, login_user)
    post_page = PostPage(browser, login_user)
    dm_page = DmPage(browser, login_user)

    login_page.login()

    REMAINING_REQUESTS, REMAINING_LIKES, REMAINING_DM = daily_request_limit, daily_like_limit, daily_dm_limit
    reset_time = datetime.now()

    while True:
        if (datetime.now() - reset_time).total_seconds() > 70000:
            print("Resetting remaining requests, likes and dm")
            reset_time = datetime.now()
            REMAINING_REQUESTS, REMAINING_LIKES, REMAINING_DM = daily_request_limit, daily_like_limit, daily_dm_limit
            messages = messages_init

        for username in user_list:
            try:
                print(f"going to target user {username}")
                over = check_user(user_page, post_page, dm_page, look_followers, keywords, username)
                if over:
                    break
            except Exception as e:
                print(e)

        if REMAINING_REQUESTS == 0 and REMAINING_LIKES == 0 and REMAINING_DM == 0:
            print("Going into sleep mode since no remaining requests, likes and dm")
            sleep(80000)


def undo_request(login_user, login_password, days):
    login_page = LoginPage(browser, login_user, login_password)
    user_page = UserPage(browser, login_user)

    login_page.login()
    usernames = find_follow_requests(login_user, days)
    print("undo people: ", usernames)

    for username in usernames:
        try:
            print(f"unfollowing {username}")

            user_page.go_user(username)
            user_page.undo_follow_request()
            delete_follow_request(login_user, username)

            sleep(random.randint(MIN_TIME, MAX_TIME))
        except Exception as e:
            print(e)


def main():
    global MIN_TIME, MAX_TIME, messages, messages_init

    filename = sys.argv[1]
    with open(f"../{filename}") as json_file:
        json_content = json.load(json_file)

        login_user = json_content["username"]
        login_password = json_content["password"]

        MIN_TIME = json_content["minTime"]
        MAX_TIME = json_content["maxTime"]

        if "UNDO_REQUEST" in json_content:
            print("undo requests")

            days = json_content["days"]
            undo_request(login_user, login_password, days)

        else:
            print("creating bot")

            user_list = json_content["targets"].split("\n")
            look_followers = json_content["lookFollowers"]
            keywords = json_content["keywords"].split("\n")
            messages = json_content["messages"]
            messages_init = json_content["messages"]

            daily_request_limit = json_content["requestLimit"]
            daily_like_limit = json_content["likeLimit"]
            daily_dm_limit = json_content["dmLimit"]

            create_process(login_user, login_password, user_list, look_followers, keywords,
                           daily_request_limit, daily_like_limit, daily_dm_limit)


if __name__ == "__main__":
    main()
