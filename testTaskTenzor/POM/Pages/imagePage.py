from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.Test import log_app as log


class ImagePage:

    def __init__(self, browser):
        self.browser = browser
        self.first_category_locator = '.PopularRequestList>div>a'
        self.text_first_category_locator = '.PopularRequestList>div>a>img'
        self.name_attribute_locator = '.PopularRequestList>div'
        self.get_attribute_text = 'data-grid-text'
        self.first_img_locator = 'img.serp-item__thumb'
        self.search_field_locator = 'input.input__control.mini-suggest__input'


    def first_category_click(self):
        click_first_category = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.first_category_locator)))
        click_first_category.click()

    def first_img_click(self):
        click_first_img = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.first_img_locator)))
        click_first_img.click()

    def assert_link_new_windows(self):
        link_new_windows = self.browser.current_url
        assert link_new_windows == 'https://yandex.ru/images/', log.logger.error('URL not https://yandex.ru/images/')
        log.logger.info('Correct URL "https://yandex.ru/images/"')

    def assert_category_display_in_the_search_field(self):
        name_first_category = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.text_first_category_locator)))
        text_first_category = name_first_category.get_attribute('alt')

        search_field = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.search_field_locator)))
        text_in_search_field = search_field.get_property("value")

        assert text_first_category == text_in_search_field, log.logger.error('The category is'
                                                                             ' not displayed in the search field')
        log.logger.info('The category is displayed in the search field')