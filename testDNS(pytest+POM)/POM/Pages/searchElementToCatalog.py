from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SearchElementToCatalog:
    def __init__(self, browser):
        self.browser = browser

        self.elements_by_dns_locator = "div[class='catalog-menu']>div"
        self.name_element_dns_locator = "h1.subcategory__page-title"

    def search_elements(self):
        lst_name_element_dns_real = []


        for i in range(14):
            elements_by_dns = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.elements_by_dns_locator)))
            elements_by_dns[i].click()
            name_element_dns = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.name_element_dns_locator))).text
            lst_name_element_dns_real.append(name_element_dns)
            time.sleep(1)
            self.browser.back()

        return lst_name_element_dns_real