from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class StartPage:

    def __init__(self, browser):
        self.browser = browser
        self.search_input_locator = 'input.search3__input'
        self.button_menu_locator = '.services-pinned__content>a'
        self.select_img_locator = 'div[data-section="all"] a:nth-child(13)'

    def send_text(self, text):
        self.search_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.search_input_locator)))
        self.search_input.send_keys(text)

    def click_enter(self):
        self.search_input.send_keys(Keys.ENTER)

    def button_menu_click(self):
        self.button_menu = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.button_menu_locator)))
        self.button_menu.click()


    def select_img(self):
        self.select_img = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.select_img_locator)))
        self.select_img.click()