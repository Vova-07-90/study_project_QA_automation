from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *

try:
    link='http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.maximize_window
    browser.get(link)
    
    def calc(x):
        return log(abs(12*sin(x)))
    
    x_element = browser.find_element(By.CSS_SELECTOR, "label>:nth-child(2)").text
    x = int(x_element)
    y = calc(x)
    
    input = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input.send_keys(y)
    
    # Прокрутка страницы вниз, что б было видно кнопку
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    checkbox = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]').click()
    

    button.click()
    
    print(browser.switch_to.alert.text)
    
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
