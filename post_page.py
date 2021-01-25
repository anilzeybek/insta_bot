from time import sleep


class PostPage:
    def __init__(self, browser):
        self.browser = browser

    def find_target_users(self, kw_list):
        # TODO: only looks the initial comments, search for every comment

        usernames = []
        comments = self.browser.find_elements_by_xpath("//article/div[3]/div[1]/ul/ul")

        for comment in comments:
            text = comment.find_element_by_xpath(".//span[@class='']").text

            if set(text.split()).intersection(set(kw_list)):
                username = comment.find_element_by_xpath(".//span/a").text
                usernames.append(username)

        return usernames

    def like_post(self):
        # TODO: implement
        pass
