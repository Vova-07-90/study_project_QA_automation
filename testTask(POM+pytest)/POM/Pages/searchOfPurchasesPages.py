from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class SearchOfPurchases():

    def __init__(self, browser):
        self.browser = browser

        self.btn_load_more = 'button#load-more'
        self.min_price = 'div[itemprop="price"]'

    def search_of_purchases(self, attribute):
        list_price = []
        my_file = open("min_price_test_rts_2.txt", "w")
        flag = True
        while flag == True:
            # задержка против капчи
            time.sleep(2)
            try:
                bth_click = self.browser.find_element(By.CSS_SELECTOR, self.btn_load_more)
                ActionChains(self.browser).move_to_element(bth_click).click(bth_click).perform()
            except:
                # кнопка больше не активна
                flag = False

        zakupki = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.min_price)))
        for i in range(len(zakupki)):
            zakupka_price = zakupki[i].get_attribute(attribute)
            list_price.append(zakupka_price)
            my_file.write(zakupka_price + '\n')
        my_file.close()

        # Записываем результат в переменную и передаем в логи
        list_price = list(map(float, list_price))
        info = f"Общая минимальная начальная цена = {sum(list_price)}, количество закупок = {len(list_price)}"
        return info