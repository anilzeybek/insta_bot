from time import sleep
from database_utils import add_follow_request


class UserPage:
    def __init__(self, browser, logged_user):
        self.browser = browser
        self.logged_user = logged_user

    def go_user(self, username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        sleep(3)

        locked_acc = self.browser.find_elements_by_xpath("//h2[text()='This Account is Private']")
        if locked_acc:
            return True

        return False

    def go_post(self, post_number):
        # TODO: post may not exist, check!
        
        line_index = post_number // 3 + 1
        post_index = (post_number - 1) % 3 + 1

        try:
            post = self.browser.find_element_by_xpath(f"//article/div[1]/div/div[{line_index}]/div[{post_index}]")
            post.click()
        except Exception as e:
            pass

        sleep(4)

    def send_follow_request(self, acc_to_follow):
        follow_button = self.browser.find_element_by_xpath("//button[@type='button' and text()='Follow']")
        follow_button.click()

        add_follow_request(self.logged_user, acc_to_follow)

        sleep(3)
