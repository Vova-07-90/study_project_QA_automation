from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():

    def __init__(self, browser):
        self.browser = browser

        self.checkbox_off_css = '.VkIdCheckbox__checkboxOn path[fill-rule="evenodd"]'
        self.insert_id_css = '.VkIdForm__input'
        self.btn_enter_css = '#index_login button>span'
        self.insert_password_css = 'input[name="password"]'
        self.btn_continue_css = 'span.vkuiButton__content>span'

    def checkbox_off(self):
        checkbox = self.browser.find_element(By.CSS_SELECTOR, self.checkbox_off_css)
        checkbox.click()

    def insert_id(self, id):
        insert = self.browser.find_element(By.CSS_SELECTOR, self.insert_id_css)
        insert.clear()
        insert.send_keys(id)

        btn_enter = self.browser.find_element(By.CSS_SELECTOR, self.btn_enter_css)
        btn_enter.click()

    def insert_password(self, password):
        insert_password = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.insert_password_css)))
        insert_password.clear()
        insert_password.send_keys(password)

        btn_continue = self.browser.find_element(By.CSS_SELECTOR, self.btn_continue_css)
        btn_continue.click()

