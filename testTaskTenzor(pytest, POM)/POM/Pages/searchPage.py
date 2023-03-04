from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:

    def __init__(self, browser):
        self.browser = browser
        self.first_page_of_search_locator = 'ul[id="search-result"]>li [target="_blank"]'

    def first_page_of_search_click(self):
        self.first_page_of_search = self.browser.find_element(By.CSS_SELECTOR, self.first_page_of_search_locator)
        self.first_page_of_search.click()

