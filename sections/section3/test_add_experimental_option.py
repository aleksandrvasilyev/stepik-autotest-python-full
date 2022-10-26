from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
browser = webdriver.Chrome(options=options)