from time import sleep
import sys
import logging


logging.basicConfig(filename='../logfile.log', level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


class LoginPage:
    def __init__(self, browser, username, password):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

        self.username = username
        self.password = password

    def login(self):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(3)

        unusual_login_error = self.browser.find_elements_by_xpath("//h2[text()='We Detected An Unusual Login Attempt']")
        if unusual_login_error:
            logging.warning("Unusual Login ERROR")
            sys.exit(1)

        not_now_button = self.browser.find_elements_by_xpath("//button[text()='Not Now']")
        if not_now_button:
            not_now_button[0].click()

        logging.warning("Successfully logged in")
        sleep(3)
