from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class WriteMessagePage():

    def __init__(self, browser):
        self.browser = browser

        self.write_message_css = '.ProfileHeaderActions__buttons>.ProfileHeaderButton:nth-child(2)>a'
        self.mail_box_css = 'div[id="mail_box_editable"]'
        self.btn_send_css = '.FlatButton__content'

    def write_message(self, message):
        write_message = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.write_message_css)))
        write_message.click()

        mail_box = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.mail_box_css)))
        mail_box.clear()
        mail_box.send_keys(message)

        btn_send = self.browser.find_element(By.CSS_SELECTOR, self.btn_send_css)
        btn_send.click()

