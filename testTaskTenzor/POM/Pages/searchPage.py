from selenium.webdriver.common.by import By
from POM.Test import log_app as log

class SearchPage:

    def __init__(self, browser):
        self.browser = browser
        self.first_page_of_search_locator = 'ul[id="search-result"]>li [target="_blank"]'
        self.link_search = 'https://yandex.ru/search'

    def assert_result_search(self):
        link_search = self.browser.current_url
        assert link_search.startswith(self.link_search), log.logger.error('Search results page not showing up')
        log.logger.info('Search results page showing up')

    def first_page_of_search_click(self):
        first_page_of_search = self.browser.find_element(By.CSS_SELECTOR, self.first_page_of_search_locator)
        first_page_of_search.click()
