import typing
from collections import namedtuple
from selenium import webdriver

from ..helpers import BaseDriver
from ..utilities.pkg_log import logger

__all__ = ["HomePage"]

HomePageLocator = namedtuple("HomePageLocator", "identifier type")


class HomePage(BaseDriver):
    _sign_in_button = HomePageLocator("//nav/div[@class='header_user_info']/a[@class='login']", "xpath")
    _women_text = "WOMEN"
    _dresses_text = "DRESSES"
    _tshirts_text = "T-SHIRTS"
    _menu_list = [_women_text, _dresses_text, _tshirts_text, ]


    _block_menu_a = HomePageLocator("//div[@id='block_top_menu']/ul/li/a", "xpath")
    _women_menu = HomePageLocator(
        f"//div[@id='block_top_menu']/ul/li/a[@title='Women']", "xpath"
    )
    _dresses_menu = HomePageLocator(
        f"//div[@id='block_top_menu']/ul/li/a[@title='Dresses']", "xpath"
    )
    _tshirts_menu = HomePageLocator(
        f"//div[@id='block_top_menu']/ul/li/a[@title='T-shirts']", "xpath"
    )

    def __init__(self, driver: typing.Union[webdriver.Firefox, webdriver.Chrome]):
        super().__init__(driver)

    def sign_in(self):
        self.click(*self._sign_in_button)

    def check_for_product_menus(self) -> bool:
        """Checks for presence of Women, Dresses and T-Shirts navigation options

        Returns:
            True if all options are present else False
        """
        product_menus = self.get_elements(
            locator_identifier=self._block_menu_a.identifier,
            locator_type=self._block_menu_a.type,
        )
        menu_texts = [product_menu.text for product_menu in product_menus]
        if menu_texts != self._menu_list:
            logger.error(f"{len(menu_texts)} Sections Returned. Sections: {menu_texts}")
            return False
        return True

    def go_to_women_section(self):
        self.click(*self._women_menu)

    def go_to_dresses_section(self):
        self.click(*self._dresses_menu)

    def go_to_tshirts_section(self):
        self.click(*self._tshirts_menu)
