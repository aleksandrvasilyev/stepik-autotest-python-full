from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

url = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Ivanov')

    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('mail@mail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    upload_file = browser.find_element(By.ID, 'file')
    upload_file.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(3)
    browser.quit()
