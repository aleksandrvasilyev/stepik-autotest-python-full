from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

url = 'http://SunInJuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element(By.ID, 'input_value').text
    res = str(log(abs(12 * sin(int(x)))))
    browser.execute_script("window.scrollBy(0, 200);")
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(res)

    input2 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    input3.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
