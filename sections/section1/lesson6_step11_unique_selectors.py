from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element_by_css_selector('.first_block > .first_class > .first')
    input1.send_keys('Ivan')

    input2 = browser.find_element_by_css_selector('.first_block > .second_class > .second')
    input2.send_keys('Martinov')

    input3 = browser.find_element_by_css_selector('.first_block > .third_class > .third')
    input3.send_keys('mail@mail.com')

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()
