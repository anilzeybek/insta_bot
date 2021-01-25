from selenium import webdriver
from login_page import LoginPage
from user_page import UserPage
from post_page import PostPage
import random
import sqlite3
from database_utils import add_blacklist, in_blacklist

LOGIN_USER = "niyazitecik"
LOGIN_PASSWORD = ".Qwerty1234"

USERS_LIST = ["matthewkheafy"]
KEYWORDS = ["the"]

browser = webdriver.Firefox(executable_path="./geckodriver")
browser.implicitly_wait(5)

login_page = LoginPage(browser, LOGIN_USER, LOGIN_PASSWORD)
user_page = UserPage(browser, LOGIN_USER)
post_page = PostPage(browser, LOGIN_USER)

conn = sqlite3.connect('database.db')


def like_or_follow_request(target_users):
    for user in target_users:
        if not in_blacklist(user):
            locked_acc = user_page.go_user(user)

            if not locked_acc:
                post_no = random.randint(1, 5)

                user_page.go_post(post_no)
                post_page.like_post(user)
            else:
                user_page.send_follow_request(user)

            add_blacklist(user)


def check_posts(username):
    locked_acc = user_page.go_user(username)

    if not locked_acc:
        for post_no in range(1, 6):
            user_page.go_post(post_no)
            target_users = post_page.find_target_users(KEYWORDS)

            like_or_follow_request(target_users)
            user_page.go_user(username)


def main():
    login_page.login()
    for username in USERS_LIST:
        check_posts(username)


if __name__ == "__main__":
    main()
