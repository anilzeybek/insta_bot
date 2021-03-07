from time import sleep


class UserPage:
    def __init__(self, browser, logged_user, database_utils):
        self.browser = browser
        self.logged_user = logged_user
        self.database_utils = database_utils

    def go_user(self, username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        sleep(3)

        locked_acc = self.browser.find_elements_by_xpath("//h2[text()='This Account is Private']")
        if locked_acc:
            return True

        return False

    def go_post(self, post_number):
        line_index = post_number // 3 + 1
        post_index = (post_number - 1) % 3 + 1

        try:
            post = self.browser.find_element_by_xpath(f"//article/div[1]/div/div[{line_index}]/div[{post_index}]")
            post.click()
        except Exception as e:
            sleep(10)

        sleep(4)

    def get_followers(self, how_many_followers):
        followers_button = self.browser.find_element_by_xpath("//a[contains(@href, 'followers')]")
        followers_button.click()
        sleep(5)

        follower_usernames = []
        followers = self.browser.find_elements_by_xpath("//ul/div/li")[:how_many_followers]

        for follower in followers:
            follower_username = follower.find_element_by_xpath('.//span/a').text
            follower_usernames.append(follower_username)

        return set(follower_usernames)

    def send_follow_request(self, acc_to_follow):
        follow_button = self.browser.find_element_by_xpath("//button[@type='button' and text()='Follow']")
        follow_button.click()

        self.database_utils.add_follow_request(self.logged_user, acc_to_follow)

        sleep(3)

    def undo_follow_request(self):
        try:
            requested_button = self.browser.find_element_by_xpath("//button[@type='button' and text()='Requested']")
            requested_button.click()
            sleep(4)

            unfollow_button = self.browser.find_element_by_xpath("//button[text()='Unfollow']")
            unfollow_button.click()
        except Exception as e:
            sleep(10)

        sleep(4)
