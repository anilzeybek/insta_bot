from time import sleep


class UserPage:
    def __init__(self, browser):
        self.browser = browser

    def go_user(self, username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        sleep(3)

        locked_acc = self.browser.find_elements_by_xpath("//h2[text()='This Account is Private']")
        if locked_acc:
            print("account is locked")
            return True

        return False

    def go_post(self, post_number):
        line_index = post_number // 3 + 1
        post_index = (post_number - 1) % 3 + 1

        post = self.browser.find_element_by_xpath(f"//article/div[1]/div/div[{line_index}]/div[{post_index}]")
        post.click()

        sleep(4)

    def send_follow_request(self):
        follow_button = self.browser.find_element_by_xpath("//button[@type='button' and text()='Follow']")
        follow_button.click()

        sleep(3)
