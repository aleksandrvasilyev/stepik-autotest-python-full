from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    inputs = browser.find_elements(By.TAG_NAME, 'input')
    for input in inputs:
        input.send_keys('123')

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
finally:
    time.sleep(3)
    browser.quit()
