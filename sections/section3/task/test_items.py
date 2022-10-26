import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_see_add_to_cart_button(browser):
    browser.get(link)
    button = browser.find_elements_by_class_name("btn-add-to-basket")
    time.sleep(5)
    assert len(button) > 0, 'не найдено'