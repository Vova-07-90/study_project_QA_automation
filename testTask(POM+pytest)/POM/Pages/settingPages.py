from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SettingPage():

    def __init__(self, browser):
        self.browser = browser
        
        self.checkbox_on = '.modal-settings-section:nth-child(1) .grid-column-4-1:nth-child(3)>input'
        
        self.checkbox_on2 = 'div.modal-settings-section:nth-child(2)>div:nth-child(3)>div>div>div:nth-child(3)>input'
        
        self.checkbox_off = 'div.modal-settings-section:nth-child(3)>div:nth-child(3)>div>div>input'
        
        self.checkbox_on3 = 'div.modal-settings-section:nth-child(3)>div:nth-child(3)>div>div:nth-child(2)>div'
        
        self.open_region = 'div.modal-settings-section:nth-child(7)>div'
        
        self.to_go_region = 'div.modal-settings-section:nth-child(7)>.plate-tabs'
        self.to_add_region = 'input[placeholder="Регион поставки"]'
        self.select_region = 'a.cstm-search__suggest'
        
        self.date_filter = 'div.modal-settings-section:nth-child(12)>div'
        self.btn_by = '.form-group>.form-group__cell:nth-child(3)'
        self.day_today = '.react-datepicker__day--today'
        
        self.btn_search = '.search__btn.bottomFilterSearch'

        
    def click_checkbox_on(self):
        element_checkbox_on = self.browser.find_element(By.CSS_SELECTOR, self.checkbox_on)
        ActionChains(self.browser).move_to_element(element_checkbox_on).click(element_checkbox_on).perform()

    def click_checkbox_on2(self):
        element_checkbox_on2 = self.browser.find_element(By.CSS_SELECTOR, self.checkbox_on2)
        ActionChains(self.browser).move_to_element(element_checkbox_on2).click(element_checkbox_on2).perform()

    def click_checkbox_off(self):
        element_checkbox_off = self.browser.find_element(By.CSS_SELECTOR, self.checkbox_off)
        ActionChains(self.browser).move_to_element(element_checkbox_off).click(element_checkbox_off).perform()

    def click_checkbox_on3(self):
        element_checkbox_on3 = self.browser.find_element(By.CSS_SELECTOR, self.checkbox_on3)
        ActionChains(self.browser).move_to_element(element_checkbox_on3).click(element_checkbox_on3).perform()

    def click_open_region(self):
        element_region = self.browser.find_element(By.CSS_SELECTOR, self.open_region)
        ActionChains(self.browser).move_to_element(element_region).click(element_region).perform()

    def insert_region(self, region):
        element_to_go_region = self.browser.find_element(By.CSS_SELECTOR, self.to_go_region)
        element_to_add_region = self.browser.find_element(By.CSS_SELECTOR, self.to_add_region)
        ActionChains(self.browser).move_to_element(element_to_go_region).send_keys_to_element(element_to_add_region,
                                                                                              region).perform()
        element_select_region = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.select_region)))
        element_select_region.click()

    def select_date(self):
        element_date_filter = self.browser.find_element(By.CSS_SELECTOR, self.date_filter)
        ActionChains(self.browser).move_to_element(element_date_filter).click(element_date_filter).perform()
        element_btn_by = self.browser.find_element(By.CSS_SELECTOR, self.btn_by)
        ActionChains(self.browser).move_to_element(element_btn_by).click(element_btn_by).perform()
        element_day_today = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.day_today)))
        element_day_today.click()

    def click_btn_search(self):
        element_btn_search = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.btn_search)))
        element_btn_search.click()
