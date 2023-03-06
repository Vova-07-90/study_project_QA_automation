from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.Pages.assertFunctionPage import AssertFunctionPage
from POM.Test import log_app as log


class StartPage:

    def __init__(self, browser):
        self.browser = browser
        self.search_input_locator = 'input.search3__input'
        self.button_menu_locator = '.services-pinned__content>a'
        self.input_box_locator = 'input.search3__input'
        self.text_insert_in_search_box = 'Тензор'
        self.suggest_input_locator = 'form.mini-suggest_open'
        self.function = AssertFunctionPage(browser)

    def send_text(self):
        self.search_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.search_input_locator)))
        self.search_input.send_keys(self.text_insert_in_search_box)

    def click_enter(self):
        self.search_input.send_keys(Keys.ENTER)

    def button_menu_click(self):
        button_menu = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.button_menu_locator)))
        button_menu.click()

    def assert_general_search_box(self):
        assert self.function.element_should_be_present(self.input_box_locator) == True,\
            log.logger.error('Element "Search" not found')
        log.logger.info('Element "Search" found')

    def assert_suggest_input(self):
        try:
            assert self.function.element_should_be_present(self.suggest_input_locator) == True
            log.logger.info('Element "Suggest" found')
        except:
            log.logger.error('Element "Suggest" not found')

    def assert_button_menu(self):
        assert self.function.element_should_be_present(self.button_menu_locator) == True, \
            log.logger.error('Element "Button menu" not found')
        log.logger.info('Element "Button menu" found')
