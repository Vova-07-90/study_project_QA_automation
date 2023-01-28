from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = 'https://www.dns-shop.ru/'
browser = webdriver.Chrome()
browser.maximize_window
browser.get(link)

lst_name_element_DNS = ['Бытовая техника', 'Красота и здоровье', 'Смартфоны и фототехника', 'ТВ, консоли и аудио', 'ПК, ноутбуки, периферия', 'Комплектующие для ПК', 'Офис и мебель', 'Сетевое оборудование', 'Отдых и развлечения', 'Инструмент и стройка', 'Садовая техника', 'Дом, декор и посуда', 'Автотовары', 'Аксессуары и услуги']
lst_name_element_DNS_real = []
for i in range(14):
    elements_by_DNS = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[class='catalog-menu']>div")))
    elements_by_DNS[i].click()
    name_element_DNS = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.subcategory__page-title"))).text
    lst_name_element_DNS_real.append(name_element_DNS)
    time.sleep(1)
    browser.back()

assert lst_name_element_DNS_real == lst_name_element_DNS, f'Имена не совпадают, вот что получилось {lst_name_element_DNS_real}'

