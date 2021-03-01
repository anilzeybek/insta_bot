from time import sleep


class HashtagPage:
    def __init__(self, browser):
        self.browser = browser

    def _load_posts(self):
        for _ in range(20):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)

    def go_hashtag(self, hashtag):
        self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}")
        sleep(1)

        self._load_posts()

    def get_post_links(self):
        links = self.browser.find_elements_by_xpath("//article/div/div/div/div/a")
        links = list(map(lambda x: x.get_attribute('href'), links))
        return links