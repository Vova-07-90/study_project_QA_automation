import pytest

from selenium import webdriver
from POM.Pages.searchElementToCatalog import SearchElementToCatalog
from POM.Pages.assertPage import AssertPage


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_dns_1(browser):
    link = 'https://www.dns-shop.ru/'
    browser.get(link)

    checklist = AssertPage()
    checklist = checklist.checklist()

    search = SearchElementToCatalog(browser)
    lst_name_element_dns_real = search.search_elements()

    assert (
    lst_name_element_dns_real == checklist, f'Имена не совпадают, вот что получилось {lst_name_element_dns_real}')
