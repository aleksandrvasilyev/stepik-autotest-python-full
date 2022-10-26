import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):
    def testmy(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')

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

        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)


if __name__ == "__main__":
    unittest.main()


# run
# python -m unittest lesson2_step13_unittest.py

