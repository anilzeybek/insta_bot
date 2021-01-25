from selenium import webdriver
from login_page import LoginPage
from user_page import UserPage
from post_page import PostPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import sqlite3


USERS_LIST = ["kadikoybelediye"]
KEYWORDS = ["the"]

browser = webdriver.Firefox(executable_path="./geckodriver")
browser.implicitly_wait(5)

login_page = LoginPage(browser)
user_page = UserPage(browser)
post_page = PostPage(browser)
actions = ActionChains(browser)
conn = sqlite3.connect('database.db')


def give_like(target_users):
    for user in target_users:
        locked_acc = user_page.go_user(user)

        if not locked_acc:
            post_no = random.randint(1, 5)
            print(f"Liking post {post_no}")

            user_page.go_post(post_no)
            post_page.like_post()
        else:
            user_page.send_follow_request()


def check_posts(username):
    locked_acc = user_page.go_user(username)

    # TODO: sor, hedef listesindeki hesap gizliyse takip et?
    if not locked_acc:
        for post_no in range(1, 6):
            user_page.go_post(post_no)
            target_users = post_page.find_target_users(KEYWORDS)

            give_like(target_users)
            user_page.go_user(username)


def main():
    login_page.login("niyazitecik", ".Qwerty1234")
    for username in USERS_LIST:
        check_posts(username)


if __name__ == "__main__":
    main()
