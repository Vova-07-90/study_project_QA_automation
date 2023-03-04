import time

import pytest
from selenium import webdriver
from POM.Pages.assertFunctionPage import AssertFunctionPage
from POM.Pages.startPage import StartPage
from POM.Pages.searchPage import SearchPage
from POM.Pages.imagePage import ImagePage


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


class TestTenzor:
    def test_search_of_yandex(self, browser):

        link = 'https://ya.ru/'
        browser.get(link)
        function = AssertFunctionPage(browser)

        # действия на startPage
        start_page = StartPage(browser)
        assert function.validation_func('input.search3__input') == True, 'Error: element "Search" not found'
        start_page.send_text(text='Тензор')
        try:
            assert function.validation_func('form.mini-suggest_open') == True
        except:
            print('Error: element "Suggest" not found')
        start_page.click_enter()


        # действия на searchPage
        link_search = browser.current_url
        assert link_search.startswith('https://yandex.ru/search'), 'Error: search results page not showing up'
        search_page = SearchPage(browser)
        search_page.first_page_of_search_click()
    

        # Действия на новой вкладке
        browser.switch_to.window(browser.window_handles[1])
        link_first_of_search = browser.current_url
        assert link_first_of_search == 'https://tensor.ru/', 'Error: another URL'


    def test_yandex_img(self, browser):

        link = 'https://ya.ru/'
        browser.get(link)
        function = AssertFunctionPage(browser)

        # Открыть меню, выбрать “Картинки”
        assert function.validation_func('.services-pinned__content>a') == True, 'Error: element "Button menu" not found'
        start_page = StartPage(browser)
        start_page.button_menu_click()
        start_page.select_img()

        # Переходим на новую вкладку и проверяем URL
        img_page = ImagePage(browser)
        browser.switch_to.window(browser.window_handles[1])
        link_new_windows = browser.current_url
        assert link_new_windows == 'https://yandex.ru/images/', 'Error: another URL'
        img_page.select_first_category()
        # Нужно Проверить, что название категории отображается в поле поиска
        img_page.select_first_img()
        # Нужно Проверить, что картинка открылась
        img_page.press_forward_button()
        # Нужно Проверить, что картинка сменилась
        img_page.press_back_button()
        # Нужно Проверить, что картинка вернулась предидущая
        time.sleep(5)
