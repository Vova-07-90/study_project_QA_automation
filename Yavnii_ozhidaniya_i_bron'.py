# Ждем нужный текст на странице
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

try:
    # Открываем страницу
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.maximize_window
    browser.get(link)
    
    # Говорим Selenium проверять в течение 12 секунд,
    # пока цена дома не уменьшится до $100
    # Жмем кнопку 
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5[id='price']"), "$100")) # ожидаем true, что бы перейти к след.шагу
    button = browser.find_element(By.CSS_SELECTOR, "button[id='book']").click()
    
    # Объявляем функцию для решения капчи
    def calc(x):
        return math.log(abs(12*math.sin(x)))
    
    # Находим число(аргумент) для передачи в функцию
    x_element = browser.find_element(By.CSS_SELECTOR, "label>.nowrap:nth-child(2)").text
    x_element = int(x_element)
    y = calc(int(x_element))
    
    # Подставляем результат капчи в поле
    input_answer = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input_answer.send_keys(y)
    
    # Нажимаем кнопку Submit
    button1 = browser.find_element(By.CSS_SELECTOR, "button[id='solve']")
    button1.click()
    
    print(browser.switch_to.alert.text)
    
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    


