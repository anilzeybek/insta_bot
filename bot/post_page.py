from time import sleep
from database_utils import add_like


class PostPage:
    def __init__(self, browser, logged_user):
        self.browser = browser
        self.logged_user = logged_user

    def _load_all_comments(self):
        for _ in range(15):
            load_comments_button = self.browser.find_elements_by_xpath("//span[@aria-label='Load more comments']")

            if load_comments_button:
                load_comments_button[0].click()
                sleep(3)
            else:
                break

    def find_target_users(self, kw_list):
        self._load_all_comments()

        usernames = []
        comments = self.browser.find_elements_by_xpath("//article/div[3]/div[1]/ul/ul")

        for comment in comments:
            text = comment.find_element_by_xpath(".//span[@class='']").text

            comment_words = text.split()
            for keyword in kw_list:
                for comment_word in comment_words:
                    if keyword.lower().strip() in comment_word.lower().strip():
                        username = comment.find_element_by_xpath(".//span/a").text
                        usernames.append(username)

                        break

        usernames = list(dict.fromkeys(usernames))
        return usernames

    def like_post(self, post_owner):
        try:
            like_button = self.browser.find_element_by_xpath("//span/*[name()='svg'][@aria-label='Like']")
            like_button.click()

            add_like(self.logged_user, post_owner)
        except Exception as e:
            sleep(10)
            return False

        sleep(3)
        return True

    def go_post(self, link):
        self.browser.get(link)
        sleep(0.2)

    def get_username(self):
        return self.browser.find_element_by_xpath("//article/header/div//span/a").text

    def close_post(self):
        close_button = self.browser.find_element_by_xpath("/html/body/div/div/button/div")
        close_button.click()
