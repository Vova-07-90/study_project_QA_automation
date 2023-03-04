from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class ImagePage:

    def __init__(self, browser):
        self.browser = browser
        self.first_category_locator = '.PopularRequestList>div>a'
        self.name_attribute_locator = '.PopularRequestList>div'
        self.get_attribute_text = 'data-grid-text'
        self.first_img_locator = 'img.serp-item__thumb'
        self.forward_button_locator = 'div.CircleButton:nth-child(4)>i'
        self.back_button_locator = 'div.CircleButton:nth-child(1)>i'

    def select_first_category(self):
        self.click_first_category = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.first_category_locator)))
        self.click_first_category.click()

    def select_first_img(self):
        self.click_first_img = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.first_img_locator)))
        self.click_first_img.click()

    def press_forward_button(self):
        self.press_button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.forward_button_locator)))
        self.press_button.click()

    def press_back_button(self):
        self.press_button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.back_button_locator)))
        self.press_button.click()
