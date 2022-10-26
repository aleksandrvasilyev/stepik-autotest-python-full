from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

url = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get(url)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button = browser.find_element_by_tag_name('button')
    button.click()

    x = browser.find_element_by_id('input_value').text
    x = calc(x)

    a = browser.find_element_by_id('answer')
    a.send_keys(x)

    button2 = browser.find_element_by_id('solve')
    button2.click()
finally:
    time.sleep(3)
    browser.quit()
