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

        post1 = self.browser.find_element_by_xpath(f"//article/div[1]/div/div[{line_index}]/div[{post_index}]")
        post1.click()

        sleep(4)
