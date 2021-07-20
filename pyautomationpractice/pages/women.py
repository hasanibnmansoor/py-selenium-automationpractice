import typing
from collections import namedtuple
from selenium import webdriver

from ..helpers import BaseDriver
from ..utilities.pkg_log import logger

__all__ = ["WomenPage"]

WomenPageLocator = namedtuple("WomenPageLocator", "identifier type")


class WomenPage(BaseDriver):
    _women_title_block = WomenPageLocator(
        "//div[@id='categories_block_left']/h2[@class='title_block']", "xpath"
    )
    _tops_filter = WomenPageLocator(
        "//*[text()='Tops']/parent::label/preceding-sibling::div/span/input[@type='checkbox']",
        "xpath",
    )
    _dresses_filter = WomenPageLocator(
        "//*[text()='Dresses']/parent::label/preceding-sibling::div/span/input[@type='checkbox']",
        "xpath",
    )
    _S_filter = WomenPageLocator(
        "//*[text()='S']/parent::label/preceding-sibling::div/span/input[@type='checkbox']",
        "xpath",
    )
    _M_filter = WomenPageLocator(
        "//*[text()='M']/parent::label/preceding-sibling::div/span/input[@type='checkbox']",
        "xpath",
    )
    _L_filter = WomenPageLocator(
        "//*[text()='L']/parent::label/preceding-sibling::div/span/input[@type='checkbox']",
        "xpath",
    )

    _27_dollar_product = WomenPageLocator(
        "//div[@class='product-container']/div[@class='right-block']/div[@class='content_price']/span[contains(text(), 27.00)]",
        "xpath",
    )
    _27_dollar_product_add_to_cart = WomenPageLocator(
        "//div[@class='product-container']/div[@class='right-block']/div[@class='content_price']/span[contains(text(), 27.00)]/parent::div/following-sibling::div[@class='button-container']/a[@title='Add to cart']",
        "xpath",
    )
    _27_dollar_product_more = WomenPageLocator(
        "//div[@class='product-container']/div[@class='right-block']/div[@class='content_price']/span[contains(text(), 27.00)]/parent::div/following-sibling::div[@class='button-container']/a[@title='View']",
        "xpath",
    )
    _27_dollar_product_colors = WomenPageLocator(
        "//div[@class='product-container']/div[@class='right-block']/div[@class='content_price']/span[contains(text(), 27.00)]/parent::div[@class='content_price']/following-sibling::div[@class='color-list-container']/ul/li",
        "xpath",
    )

    def __init__(self, driver: typing.Union[webdriver.Firefox, webdriver.Chrome]):
        super().__init__(driver)

    def check_for_women_sideblock_title(self) -> bool:
        """Checks for Presence of Women in the Sideblock Title as a verification of being in Women Page

        Returns:
            True/False
        """
        return self.is_element_visible(self._women_title_block.identifier, self._women_title_block.type) is not None

    def _select_filter(self, filter_element_locator: WomenPageLocator):
        self.click(filter_element_locator.identifier, filter_element_locator.type)

    def select_S(self):
        self._select_filter(self._S_filter)
    
    def select_Tops(self):
        self._select_filter(self._tops_filter)

    def hover_over_product(self, product_locator: WomenPageLocator):
        self.hover_over(product_locator.identifier, product_locator.type)
    
    def _add_to_cart(self, add_to_cart_locator: WomenPageLocator):
        self.wait_until_clickable_and_click(add_to_cart_locator.identifier, add_to_cart_locator.type)

    def _view_product_details(self, details_locator: WomenPageLocator):
        self.wait_until_clickable_and_click(details_locator.identifier, details_locator.type)

    def add_27_dollar_product_to_cart(self):
        self.hover_over_product(self._27_dollar_product)
        self._add_to_cart(self._27_dollar_product_add_to_cart)
    
    def view_details_of_27_dollar_product(self):
        self.hover_over_product(self._27_dollar_product)
        self._view_product_details(self._27_dollar_product_more)

    def num_of_colors_for_27_dollar_product(self) -> int:
        colors = self.get_elements(*self._27_dollar_product_colors)
        return len(colors)
