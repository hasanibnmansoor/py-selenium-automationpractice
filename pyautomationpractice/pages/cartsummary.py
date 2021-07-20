
import typing
from collections import namedtuple
from selenium import webdriver

from ..helpers import BaseDriver
from ..utilities.pkg_log import logger

__all__ = ["CartSummary"]

CartSummaryLocator = namedtuple('CartSummaryLocator', 'identifier type')


class CartSummary(BaseDriver):
    _cart_summary = CartSummaryLocator("cart_title", "id")
    _total_price = CartSummaryLocator("total_price", "id")
    _total_product = CartSummaryLocator("total_product", "id")
    _total_shipping = CartSummaryLocator("total_shipping", "id")
    _proceed_to_checkout = CartSummaryLocator("//a[contains(@class, 'standard-checkout')]", "xpath")
    _continue_shopping = CartSummaryLocator("//a[@title='Continue shopping']", "xpath")

    def __init__(self, driver: typing.Union[webdriver.Firefox, webdriver.Chrome]):
        super().__init__(driver)

    def proceed_to_checkout(self):
        logger.info(f"Proceeding to Checkout from {self.__class__.__name__} page")
        self.click(*self._proceed_to_checkout)

    def continue_shopping(self):
        self.click(*self._continue_shopping)

    def total_product_price(self) -> str:
        return self.get_element(*self._total_product).text

    def total_shipping_price(self) -> str:
        return self.get_element(*self._total_shipping).text

    def total_price(self) -> str:
        return self.get_element(*self.total_price).text

    
    