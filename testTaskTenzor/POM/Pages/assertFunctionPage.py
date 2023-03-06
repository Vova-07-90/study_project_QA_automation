from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AssertFunctionPage:

    def __init__(self, browser):
        self.browser = browser

    def element_should_be_present(self, locator):
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except:
            return False
