from time import sleep


class HashtagPage:
    def __init__(self, browser):
        self.browser = browser

    def load_posts(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)

    def go_hashtag(self, hashtag):
        self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}")
        sleep(0.5)

    def get_post_links(self):
        posts = self.browser.find_elements_by_xpath("//article/div/div/div/div/a")
        return posts
