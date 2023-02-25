from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SearchFriendPage():

    def __init__(self, browser):
        self.browser = browser

        self.my_friend_css = 'a[href="/friends"] span'
        self.search_friends_css = 'input[id="s_search"]'
        self.select_friend_css = 'Vova Ovchinnikov'

    def search_friend(self, name):
        my_friend = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.my_friend_css)))
        ActionChains(self.browser).move_to_element(my_friend).click(my_friend).perform()

        search_friends = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.search_friends_css)))
        search_friends.clear()
        search_friends.send_keys(name)

        select_friend = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, name)))
        ActionChains(self.browser).move_to_element(select_friend).click(select_friend).perform()


