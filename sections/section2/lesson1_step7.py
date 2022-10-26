from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

try:
    url = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    x = x.get_attribute('valuex')
    res = str(log(abs(12 * sin(int(x)))))

    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(res)

    input2 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    input3.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
finally:
    time.sleep(3)
    browser.quit()
