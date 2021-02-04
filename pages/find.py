from selenium.webdriver.common.by import By

class ImdbFindPage:
    
    SEARCH_PHRASE = (By.CSS_SELECTOR, 'span.findSearchTerm')
    RESULT_LINKS = (By.CSS_SELECTOR ,'td.result_text > a')

    def __init__(self, browser):
        self.browser = browser

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_PHRASE)
        value = search_input.text
        # value = serch_input.get_attribute('value') # for getting filled text field
        return value
    
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def select_title(self):
        self.browser.find_element(*self.RESULT_LINKS).click()