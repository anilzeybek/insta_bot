from selenium import webdriver
from login_page import LoginPage
from user_page import UserPage
from post_page import PostPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


USERS_LIST = ["matthewkheafy"]
KEYWORDS = ["the"]

browser = webdriver.Firefox(executable_path="./geckodriver")
browser.implicitly_wait(5)

login_page = LoginPage(browser)
user_page = UserPage(browser)
post_page = PostPage(browser)
actions = ActionChains(browser)


def give_like(target_users):
    print(target_users)


def check_posts(username):
    user_page.go_user(username)

    for post_no in range(1, 6):
        user_page.go_post(post_no)
        target_users = post_page.find_target_users(KEYWORDS)

        give_like(target_users)
        user_page.go_user(username)


def main():
    login_page.login("anil.z", ".Klmyok123")
    for username in USERS_LIST:
        check_posts(username)


if __name__ == "__main__":
    main()
