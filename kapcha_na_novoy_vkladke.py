# Переход на новую вкладку и прохождение капчи

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

try:
    # Открываем страницу
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.maximize_window
    browser.get(link)
    
    # Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Переключаемся на новую вкладку
    x = browser.window_handles
    new_window = x[1]  # из массива открытых вкладок присваиваем вторую вкладку переменной
    browser.switch_to.window(new_window) # переключение на новую вкладку
    
    # Решаем капчу
    def calc(x):
        return math.log(abs(12*math.sin(x)))
    
    # Считываем значение(текст) для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "label>.nowrap:nth-child(2)").text
    x_element = int(x_element)
    y = calc(x_element)
    
    # Подставляем ответ (y) в поле для ответа
    input = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input.send_keys(y)
    
    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    
    print(browser.switch_to.alert.text)
    
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()