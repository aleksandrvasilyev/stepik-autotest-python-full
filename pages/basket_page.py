from .base_page import BasePage
from .locators import ShoppingCartLocators


class BasketPage(BasePage):
    def check_if_zero_products_in_cart(self):
        zero_products = self.is_not_element_present(*ShoppingCartLocators.ZERO_PRODUCTS)
        assert zero_products

    def check_if_cart_is_empty(self):
        empty_text = self.is_element_present(*ShoppingCartLocators.EMPTY_CART)
        assert empty_text
