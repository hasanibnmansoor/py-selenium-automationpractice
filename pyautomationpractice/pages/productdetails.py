import typing
from collections import namedtuple
from selenium import webdriver

from ..helpers import BaseDriver
from ..utilities.pkg_log import logger

__all__ = ["ProductDetails"]

ProductDetailsPageLocator = namedtuple("ProductDetailsPageLocator", "identifier type")


class ProductDetails(BaseDriver):
    _add_to_cart_btn = ProductDetailsPageLocator("//*[@id='add_to_cart']/button[@name='Submit']", "xpath")
    _quantity_input = ProductDetailsPageLocator("quantity_wanted", "id")
    _quantity_increase = ProductDetailsPageLocator("//*[@id='quantity_wanted_p']/a[contains(@class, 'button-plus')]", "xpath")
    _quantity_decrease = ProductDetailsPageLocator("//*[@id='quantity_wanted_p']/a[contains(@class, 'button-minus')]", "xpath")
    _color_list_container = ProductDetailsPageLocator("color_to_pick_list", "id")
    _not_selected_color = ProductDetailsPageLocator("//*[@id='color_to_pick_list']/li[not(contains(@class, 'selected'))]", "xpath")

    def __init__(self, driver: typing.Union[webdriver.Firefox, webdriver.Chrome]):
        super().__init__(driver)

    def add_to_cart(self):
        self.click(*self._add_to_cart_btn)

    def change_color(self):
        self.click(*self._not_selected_color)

    def change_size(self):
        pass

    def change_color_and_add_to_cart(self):
        self.change_color()
        self.add_to_cart()
