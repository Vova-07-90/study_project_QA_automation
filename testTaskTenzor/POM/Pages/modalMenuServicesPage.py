from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ModalMenuServicesPage:

    def __init__(self, browser):
        self.browser = browser
        self.select_img_locator = 'div[data-section="all"] a:nth-child(13)'

    def pictures_click(self):
        pictures_select = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.select_img_locator)))
        pictures_select.click()

    def switch_to_img_page(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
