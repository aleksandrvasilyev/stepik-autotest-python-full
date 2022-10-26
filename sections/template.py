from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://google.com'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element(By.CLASS_NAME, 'name')
    input1.send_keys('Ivan')

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
finally:
    time.sleep(3)
    browser.quit()
