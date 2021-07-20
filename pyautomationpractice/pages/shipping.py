import typing
from collections import namedtuple
from selenium import webdriver

from ..helpers import BaseDriver
from ..utilities.pkg_log import logger

__all__ = ["Shipping"]

ShippingLocator = namedtuple('ShippingLocator', 'identifier type')


class Shipping(BaseDriver):
    _terms_condition_checkbox = ShippingLocator("cgv", "id")
    _proceed_to_checkout_btn = ShippingLocator("//button[@name='processCarrier']", "xpath")
    _continue_shopping_tag = ShippingLocator("//a[@title='Previous']", "xpath")

    def __init__(self, driver: typing.Union[webdriver.Firefox, webdriver.Chrome]):
        super().__init__(driver)

    def _proceed_to_checkout(self):
        self.click(*self._proceed_to_checkout_btn)

    def _continue_shopping(self):
        self.click(*self._continue_shopping_tag)

    def _accept_terms(self):
        self.click(*self._terms_condition_checkbox)

    def proceed_to_checkout(self):
        self._accept_terms()
        self._proceed_to_checkout()
