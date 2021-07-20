import typing
from collections import namedtuple
from selenium import webdriver

from ..helpers import BaseDriver
from ..utilities.pkg_log import logger

__all__ = ["CartModal"]

CartModalLocator = namedtuple("CartModalLocator", "identifier type")


class CartModal(BaseDriver):
    _product_added_to_cart_element = CartModalLocator("//h2[normalize-space()='Product successfully added to your shopping cart']", "xpath")
    _proceed_to_checkout_button = CartModalLocator("//div[@class='button-container']/a[@title='Proceed to checkout']", "xpath")

    def __init__(self, driver: typing.Union[webdriver.Firefox, webdriver.Chrome]):
        super().__init__(driver)

    def verify_product_added_to_cart_success_message(self):
        return self.is_element_visible(*self._product_added_to_cart_element) is not None

    def verify_number_of_items_in_cart_message(self):
        pass

    def verify_product_price_displayed(self):
        pass

    def verify_proceed_to_checkout_button(self):
        return self.is_element_visible(*self._proceed_to_checkout_button) is not None

    def verify_continue_shopping_button(self):
        pass

    def proceed_to_checkout(self):
        logger.info(f"Proceeding to Checkout from {self.__class__.__name__}....")
        self.click(*self._proceed_to_checkout_button)

    def continue_shopping(self):
        pass

    