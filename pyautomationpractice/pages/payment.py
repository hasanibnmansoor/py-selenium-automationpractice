import typing
from collections import namedtuple
from selenium import webdriver

from ..helpers import BaseDriver
from ..utilities.pkg_log import logger

__all__ = ["Payment"]

PaymentLocator = namedtuple('PaymentLocator', 'identifier type')


class Payment(BaseDriver):
    _pay_by_bankwire = PaymentLocator("//a[@class='bankwire' and @title='Pay by bank wire']", "xpath")
    _pay_by_check = PaymentLocator("//a[@class='cheque' and @title='Pay by check.']", "xpath")
    _continue_shopping = PaymentLocator("//a[@title='Previous']", "xpath")
    _i_confirm_my_order = PaymentLocator("//*[@id='cart_navigation']/button[@type='submit' and ./span[text()='I confirm my order']]", "xpath")
    _order_confirmation_text = PaymentLocator("//*[text()='Your order on My Store is complete.']", "xpath")

    def __init__(self, driver: typing.Union[webdriver.Firefox, webdriver.Chrome]):
        super().__init__(driver)

    def continue_shopping(self):
        self.click(*self._continue_shopping)

    def confirm_order(self):
        self.click(*self._i_confirm_my_order)

    def verify_order_confirmation(self) -> bool:
        return self.get_element(*self._order_confirmation_text) is not None

    def pay_by_bankwire(self):
        self.click(*self._pay_by_bankwire)

    def pay_by_check(self):
        self.click(*self._pay_by_check)

    def pay_by_bankwire_and_confirm_order_placed(self) -> bool:
        self.pay_by_bankwire()
        self.confirm_order()
        return self.verify_order_confirmation()

