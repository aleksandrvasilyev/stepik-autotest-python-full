from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

url = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, 'input_value').text
    res = str(log(abs(12 * sin(int(x)))))
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(res)

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()



finally:
    time.sleep(5)
    browser.quit()
