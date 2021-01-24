from time import sleep
from selenium import webdriver


def main():
    browser = webdriver.Firefox(executable_path="./geckodriver")
    browser.implicitly_wait(5)

    login_page = LoginPage(browser)
    login_page.login("anil.z", ".Klmyok123")

    user_page = UserPage(browser)
    user_page.go_user(user_id)


if __name__ == "__main__":
    main()
