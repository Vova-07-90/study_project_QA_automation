import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import logging

class TestRts(unittest.TestCase):
    def test_rts(self):  
        browser = webdriver.Chrome()
        link = "https://www.rts-tender.ru/"
        browser.maximize_window()
        browser.get(link)
        logging.basicConfig(level=logging.INFO, filename="py_log_test_rts",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
        
        # в футере переходим 223-ФЗ - Поставщикам
        element_futer = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/zakupki-223/participants-223"]'))).click()
        
        # На новой странице кликаем Расширенный поиск
        element_poisk = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/poisk/poisk-223-fz/"]'))).click()
        
        # На новой странице кликаем вкладку "настроить"
        element_settings = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.filter__open-modal'))).click()
        time.sleep(3)
        
        # В разделе "быстрые настройки" выбираем "исключить совместные закупки"
        element_checkbox_add = browser.find_element(By.CSS_SELECTOR, '.modal-settings-section:nth-child(1) .grid-column-4-1:nth-child(3)>input')
        ActionChains(browser).move_to_element(element_checkbox_add).click(element_checkbox_add).perform()
        
        # В разделе "правило проведения" выбираем "615-ПП ФР"
        element_checkbox_add2 = browser.find_element(By.CSS_SELECTOR, 'div.modal-settings-section:nth-child(2)>div:nth-child(3)>div>div>div:nth-child(3)>input')
        ActionChains(browser).move_to_element(element_checkbox_add2).click(element_checkbox_add2).perform()
        
        # В разделе "статус" деактивируем чекбокс "Активные" и активируем "Определение победителя"
        element_checkbox_off = browser.find_element(By.CSS_SELECTOR, 'div.modal-settings-section:nth-child(3)>div:nth-child(3)>div>div>input')
        ActionChains(browser).move_to_element(element_checkbox_off).click(element_checkbox_off).perform()
        element_checkbox_on = browser.find_element(By.CSS_SELECTOR, 'div.modal-settings-section:nth-child(3)>div:nth-child(3)>div>div:nth-child(2)>div')
        ActionChains(browser).move_to_element(element_checkbox_on).click(element_checkbox_on).perform()
        
        
        # Открываем раздел "Регион поставки" и выбираем Алтайский край
                # находим и открываем вкладку "Регион поставки"
        element_open = browser.find_element(By.CSS_SELECTOR, 'div.modal-settings-section:nth-child(7)>div')
        ActionChains(browser).move_to_element(element_open).click(element_open).perform()
                # Вставляем текст Алтайский край
        element_to_go = browser.find_element(By.CSS_SELECTOR, 'div.modal-settings-section:nth-child(7)>.plate-tabs')
        element_to_add = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Регион поставки"]')
        ActionChains(browser).move_to_element(element_to_go).send_keys_to_element(element_to_add, 'алтайский край').perform()
                # Выбираем Алтайский край в выпадающей вкладке
        element_to_select = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.cstm-search__suggest')))
        element_to_select.click()
        
        # Настраиваем фильтр по датам
                # находим и открываем вкладку "Фильтры по датам"
        element_open = browser.find_element(By.CSS_SELECTOR, 'div.modal-settings-section:nth-child(12)>div')
        ActionChains(browser).move_to_element(element_open).click(element_open).perform()
                # выбираем и кликаем подача заявок по сегодняшний день
        element_to_go_click = browser.find_element(By.CSS_SELECTOR, '.form-group>.form-group__cell:nth-child(3)')
        ActionChains(browser).move_to_element(element_to_go_click).click(element_to_go_click).perform()
                # в открывшейся вкладке Календаря выбираем сегодняшнюю дату
        element_date_today = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.react-datepicker__day--today')))
        element_date_today.click()
        
        # Нажимаем найти для поиска результатов
        element_button_search = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.search__btn.bottomFilterSearch')))
        ActionChains(browser).move_to_element(element_button_search).click(element_button_search).perform()
        
        
        # Создаем список и файл куда сохраняем цены
        list_price = []
        my_file = open("min_price_test_rts.txt", "w")
        
        # Запускаем цикл. Пока кнопка Вперед активна. Считываем нужную информацию,
        # записываем ее в файл, нажимаем кнопку "Вперед". Если кнопка неактивна, 
        # значитмы находимся на последней странице. Меняем флаг и заканчиваем цикл.
        flag = True
        while flag == True:
            time.sleep(1)
            zakupki = WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[itemprop="price"]')))
            for i in range(len(zakupki)):
                zakupka_price = zakupki[i].get_attribute('content')
                list_price.append(zakupka_price)
                my_file.write(zakupka_price + '\n')
            try:
                bth_click = browser.find_element(By.CSS_SELECTOR, '#pager li a.page-link.next')
                ActionChains(browser).move_to_element(bth_click).click(bth_click).perform()   
            except:
                flag = False
                print('Кнопка не активна')
        my_file.close()
        
        # Записываем результат в логи
        list_price = list(map(float, list_price))
        logging.info(f"Общая минимальная начальная цена = {sum(list_price)}, количество закупок = {len(list_price)}")
        
if __name__ == "__main__":
    unittest.main()    
    
    
    
    