import typing
from collections import namedtuple
from selenium import webdriver

from ..helpers import BaseDriver
from ..utilities.pkg_log import logger

__all__ = ["Authenticate"]

AuthenticatePageLocator = namedtuple("AuthenticatePageLocator", "identifier type")


class Authenticate(BaseDriver):
    _login_username_elem = AuthenticatePageLocator("email", "id")
    _login_password_elem = AuthenticatePageLocator("passwd", "id")
    _sign_in_button = AuthenticatePageLocator("SubmitLogin", "id")

    def __init__(self, driver: typing.Union[webdriver.Firefox, webdriver.Chrome]):
        super().__init__(driver)

    def _enter_username(self, username: str):
        self.enter_text(*self._login_username_elem, username)

    def _enter_password(self, password: str):
        self.enter_text(*self._login_password_elem, password)

    def _click_sign_in_button(self):
        self.click(*self._sign_in_button)

    def sign_in(self, username: str, password: str):
        self._enter_username(username)
        self._enter_password(password)
        self._click_sign_in_button()

    