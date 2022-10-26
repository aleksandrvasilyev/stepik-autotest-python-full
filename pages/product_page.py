from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_LINK)
        add.click()

    def checking(self):
        self.browser.implicitly_wait(5)
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        success_added = self.browser.find_element(*ProductPageLocators.SUCCESS_ADDED).text
        success_cost = self.browser.find_element(*ProductPageLocators.SUCCESS_COST).text
        assert success_added == product_title and success_cost == product_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_second(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
