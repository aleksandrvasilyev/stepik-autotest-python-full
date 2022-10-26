from selenium import webdriver
# import time
import unittest


class TestUI(unittest.TestCase):

    def test_first(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector('.first_block .form-control.first')
        input2 = browser.find_element_by_css_selector('.first_block .form-control.second')
        input3 = browser.find_element_by_css_selector('.first_block .form-control.third')
        input4 = browser.find_element_by_css_selector('.second_block .form-control.first')
        input5 = browser.find_element_by_css_selector('.second_block .form-control.second')
        input1.send_keys('Alex')
        input2.send_keys('Vasilyev')
        input3.send_keys('name@domain.com')
        input4.send_keys('+38012345678')
        input5.send_keys('Kharkov, pr. Peremohy 89')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # time.sleep(1)
        success_text = browser.find_element_by_tag_name("h1")
        self.assertEqual(success_text.text, 'Congratulations! You have successfully registered!', 'Error!')
        browser.quit()

    def test_second(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        browser.get(link)

        input1 = browser.find_element_by_css_selector('.first_block > .first_class > .first')
        input2 = browser.find_element_by_css_selector('.first_block > .second_class > .second')
        input3 = browser.find_element_by_css_selector('.first_block > .third_class > .third')
        input1.send_keys('Name')
        input2.send_keys('Surname')
        input3.send_keys('Email')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        success_text = browser.find_element_by_tag_name("h1")
        self.assertEqual(success_text.text, 'Congratulations! You have successfully registered!', 'Error!')
        browser.quit()


if __name__ == "__main__":
    unittest.main()