import typing
from collections import namedtuple
from selenium import webdriver

from ..helpers import BaseDriver
from ..utilities.pkg_log import logger

__all__ = ["Address"]

AddressLocator = namedtuple('AddressLocator', 'identifier type')


class Address(BaseDriver):
    _proceed_to_checkout = AddressLocator("//button[@name='processAddress']", "xpath")
    _continue_shopping = AddressLocator("//a[@title='Previous']", "xpath")

    def __init__(self, driver: typing.Union[webdriver.Firefox, webdriver.Chrome]):
        super().__init__(driver)

    def proceed_to_checkout(self):
        logger.info(f"Proceeding to Checkout from {self.__class__.__name__} page")
        self.click(*self._proceed_to_checkout)

    def continue_shopping(self):
        self.click(*self._continue_shopping)
