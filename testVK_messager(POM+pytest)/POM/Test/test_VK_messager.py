import pytest
from selenium import webdriver
from POM.Pages.loginPage import LoginPage
from POM.Pages.searchFriendPage import SearchFriendPage
from POM.Pages.writeMessagePage import WriteMessagePage
import time

@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()

def test_vk_messager(browser):
    link = 'https://vk.com/'
    browser.get(link)

    login = LoginPage(browser)
    login.checkbox_off()
    login.insert_id('89787672507')
    login.insert_password('ledzeppelin23')

    search = SearchFriendPage(browser)
    search.search_friend('Vova Ovchinnikov')

    write = WriteMessagePage(browser)
    write.write_message('hello')

    time.sleep(3)
    browser.save_screenshot("screenshot.png")
