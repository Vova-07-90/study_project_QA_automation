import unittest
from selenium import webdriver
import logging
from POM.Pages.pathToSettingPages import PathToSettingPage
from POM.Pages.settingPages import SettingPage
from POM.Pages.searchOfPurchasesPages import SearchOfPurchases

class TestRts2(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(3)

    def test_path_to_settings(self):
        logging.basicConfig(level=logging.INFO, filename="py_log_test_rts_2.log", filemode="w",
                            format="%(asctime)s %(levelname)s %(message)s")

        browser = self.browser
        browser.get("https://www.rts-tender.ru/")

        path = PathToSettingPage(browser)
        path.click_futer()
        path.click_tab_search()
        path.click_tab_setting()

        setting = SettingPage(browser)
        setting.click_checkbox_on()
        setting.click_checkbox_on2()
        setting.click_checkbox_off()
        setting.click_checkbox_on3()
        setting.click_open_region()
        setting.insert_region('алтайский край')
        setting.select_date()
        setting.click_btn_search()

        cycle = SearchOfPurchases(browser)
        logging.info(cycle.search_of_purchases('content'))


    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()