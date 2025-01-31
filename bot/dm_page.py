from time import sleep
import common


class DmPage:
    def __init__(self, browser, logged_user, database_utils):
        self.browser = browser
        self.logged_user = logged_user
        self.database_utils = database_utils

    def send_message(self, user, message):
        self.browser.get("https://www.instagram.com/direct/new/")
        sleep(3)

        username_input = self.browser.find_element_by_xpath("//input[@placeholder='Search...']")
        username_input.send_keys(user)

        common.not_now(self.browser)

        user_link = self.browser.find_element_by_xpath(f"//div[text()='{user}']")
        user_link.click()
        sleep(5)

        next_button = self.browser.find_element_by_xpath("//div[text()='Next']")
        next_button.click()
        sleep(5)

        message_input = self.browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
        message_input.send_keys(message)
        sleep(5)

        send_button = self.browser.find_element_by_xpath("//button[text()='Send']")
        send_button.click()
        sleep(5)

        self.database_utils.add_dm(self.logged_user, user, message)
