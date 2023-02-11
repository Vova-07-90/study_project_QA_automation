from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class PathToSettingPage():

    def __init__(self, browser):
        self.browser = browser

        self.futer_css = 'a[href="/zakupki-223/participants-223"]'
        self.tab_search_css = 'a[href="/poisk/poisk-223-fz/"]'
        self.tab_setting_css = 'span.filter__open-modal'

    def click_futer(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.futer_css))).click()

    def click_tab_search(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.tab_search_css))).click()

    def click_tab_setting(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.tab_setting_css))).click()