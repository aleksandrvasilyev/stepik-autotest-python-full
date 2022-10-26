from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    num1 = browser.find_element(By.ID, 'num1').text

    num2 = browser.find_element(By.ID, 'num2').text

    summ = str(int(num1) + int(num2))

    val = browser.find_element(By.CSS_SELECTOR, f"[value='{summ}']").click()


    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
finally:
    time.sleep(3)
    browser.quit()


