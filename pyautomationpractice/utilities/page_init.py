from pyautomationpractice.pages.shipping import Shipping
from pyautomationpractice.pages.payment import Payment
from pyautomationpractice.pages.productdetails import ProductDetails
from pyautomationpractice.pages.address import Address
from pyautomationpractice.pages.authentication import Authenticate
from pyautomationpractice.pages.cartsummary import CartSummary
from pyautomationpractice.pages.cartmodal import CartModal
from pyautomationpractice.pages.women import WomenPage
from pyautomationpractice.pages.home import HomePage
from typing import Union
from collections import namedtuple
from selenium import webdriver
from pyautomationpractice.pages import *


PageObjects = namedtuple('PageObjects', ['home', 'women', 'cartmodal', 'cartsummary', 'auth', 'address', 'productdetails', 'payment', 'shipping'])

def init(driver: Union[webdriver.Firefox, webdriver.Chrome]) -> PageObjects:
    return PageObjects(
        home= HomePage(driver),
        women = WomenPage(driver),
        cartmodal=CartModal(driver),
        cartsummary=CartSummary(driver),
        auth=Authenticate(driver),
        address=Address(driver),
        productdetails=ProductDetails(driver),
        payment=Payment(driver),
        shipping=Shipping(driver),
    )
