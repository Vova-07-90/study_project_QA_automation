from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.Test import log_app as log


class ModalMenuWithPicturesPage:

    def __init__(self, browser):
        self.browser = browser
        self.forward_button_locator = 'div.CircleButton:nth-child(4)>i'
        self.back_button_locator = 'div.CircleButton:nth-child(1)>i'
        self.modal_windows_pic_locator = '.Modal.Modal_visible'
        self.url_pic_locator = '.MMImageContainer>img'

    def press_forward_button(self):
        press_button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.forward_button_locator)))
        press_button.click()

    def press_back_button(self):
        press_button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.back_button_locator)))
        press_button.click()

    def assert_picture_opened_after_click(self):
        modal_window = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.modal_windows_pic_locator)))
        modal_window.is_displayed()
        try:
            log.logger.info('Picture opened after click')
        except:
            log.logger.error('Picture did not opened after click')

    def safe_link_first_pic(self):
        url_first_pic = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.url_pic_locator)))
        global text_first_url
        text_first_url = url_first_pic.get_attribute('src')

    def safe_link_second_pic(self):
        url_second_pic = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.url_pic_locator)))
        global text_second_url
        text_second_url = url_second_pic.get_attribute('src')

    def assert_picture_changed(self):
        assert text_first_url != text_second_url, log.logger.error('The picture has not changed')
        log.logger.info('The picture is changed')

    def assert_returned_the_first_picture(self):
        re_url_first_pic = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.url_pic_locator)))
        re_text_first_url = re_url_first_pic.get_attribute('src')
        assert text_first_url == re_text_first_url, log.logger.error('Pictures don.t match')
        log.logger.info('Picture returned the first picture')
