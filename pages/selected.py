from selenium.webdriver.common.by import By

class ImdbSelectedPage:

    MOVIE_TITLE = (By.CSS_SELECTOR ,'div.title_wrapper > h1')

    def __init__(self, browser):
        self.browser = browser

    def title(self):
        return self.browser.title

    def movie_name(self):
        return self.browser.find_element(*self.MOVIE_TITLE).text
