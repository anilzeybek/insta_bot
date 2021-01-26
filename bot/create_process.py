from selenium import webdriver
from login_page import LoginPage
from user_page import UserPage
from post_page import PostPage
import random
from database_utils import add_blacklist, in_blacklist
from datetime import datetime
from time import sleep
import sys
import json

REMAINING_REQUESTS = 0
REMAINING_LIKES = 0


def like_or_follow_request(user_page, post_page, target_users):
    global REMAINING_REQUESTS, REMAINING_LIKES

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
            elif REMAINING_REQUESTS > 0:
                user_page.send_follow_request(user)

                add_blacklist(user)
                REMAINING_REQUESTS -= 1

                print(f"remaining likes: {REMAINING_REQUESTS}")


def check_posts(user_page, post_page, keywords, username):
    global REMAINING_REQUESTS, REMAINING_LIKES

    locked_acc = user_page.go_user(username)
    if not locked_acc:
        for post_no in range(1, 6):
            if REMAINING_REQUESTS > 0 or REMAINING_LIKES > 0:
                user_page.go_post(post_no)
                target_users = post_page.find_target_users(keywords)

                like_or_follow_request(user_page, post_page, target_users)
                user_page.go_user(username)

            else:
                return


def create_process(login_user, login_password, user_list, keywords, daily_request_limit, daily_like_limit):
    global REMAINING_REQUESTS, REMAINING_LIKES

    browser = webdriver.Firefox(executable_path="../geckodriver")
    browser.implicitly_wait(5)

    login_page = LoginPage(browser, login_user, login_password)
    user_page = UserPage(browser, login_user)
    post_page = PostPage(browser, login_user)

    login_page.login()

    REMAINING_REQUESTS, REMAINING_LIKES = daily_request_limit, daily_like_limit
    reset_time = datetime.now()

    while True:
        if REMAINING_REQUESTS == 0 and REMAINING_LIKES == 0:
            print("Going into sleep mode since no remaining requests and likes")
            sleep(86400)

        if (datetime.now() - reset_time).total_seconds() > 86400:
            print("Resetting remaining requests and remaining likes")
            reset_time = datetime.now()
            REMAINING_REQUESTS, REMAINING_LIKES = daily_request_limit, daily_like_limit

        for username in user_list:
            try:
                check_posts(user_page, post_page, keywords, username)
            except Exception as e:
                print(e)


def main():
    filename = sys.argv[1]
    with open(f"../{filename}") as json_file:
        json_content = json.load(json_file)

        login_user = json_content["username"]
        login_password = json_content["password"]

        user_list = json_content["targets"].split("\n")
        keywords = json_content["keywords"].split("\n")

        daily_request_limit = json_content["requestLimit"]
        daily_like_limit = json_content["likeLimit"]

        create_process(login_user, login_password, user_list, keywords, daily_request_limit, daily_like_limit)


if __name__ == "__main__":
    main()
