from time import sleep


class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        sleep(3)

        now_now_button = self.browser.find_element_by_xpath("//button[@type='button' and text()='Not Now']")
        now_now_button.click()

        sleep(3)

        now_now_button = self.browser.find_element_by_xpath("//button[text()='Not Now']")
        now_now_button.click()

        sleep(3)
