from time import sleep


class PostPage:
    def __init__(self, browser):
        self.browser = browser

    def _load_all_comments(self):
        while True:
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

            if set(text.split()).intersection(set(kw_list)):
                username = comment.find_element_by_xpath(".//span/a").text
                usernames.append(username)

        return usernames

    def like_post(self):
        try:
            like_button = self.browser.find_element_by_xpath("//span/*[name()='svg'][@aria-label='Like']")
            like_button.click()
        except Exception as e:
            pass

        sleep(3)
