from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest

txt = ''
@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
# @pytest.mark.parametrize('links', ["236895"])
def test_answer(browser, links):
    link = f"https://stepik.org/lesson/{links}/step/1"
    answer = str(math.log(int(time.time())))
    browser.get(link)
    area = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea")))
    area.send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

    message = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
    if message.text != "Correct!":
        global txt
        txt += message.text
    assert message.text == "Correct!"

    # time.sleep(1)


print(txt)
