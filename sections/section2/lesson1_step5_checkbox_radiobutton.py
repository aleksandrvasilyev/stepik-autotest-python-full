from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

try:
    url = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text
    # x = browser.find_element_by_id('input_value').text
    res = str(log(abs(12 * sin(int(x)))))

    input1 = browser.find_element(By.CLASS_NAME, 'form-control')
    input1.send_keys(res)

    input2 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    input3.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
finally:
    time.sleep(3)
    browser.quit()
