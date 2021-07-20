""" webdriver_.py
"""
import typing

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from .pkg_log import logger

__all__ = [
    "get_driver_for_browser",
]


def get_driver_for_browser(
    browser: str = "Chrome",
) -> typing.Union[webdriver.Firefox, webdriver.Chrome]:
    """get_driver_for_browser
    Args:
        browser: Browser Name required for Test. Support "Firefox" and "Chrome".
        Defaults to Chrome.
    Returns:
        Based on user-provided browser name, returns respective Driver instance.
    """
    browser = browser.lower()
    if browser == "firefox":
        logger.info(
            "Initiating Driver Instance for Firefox using GeckoDriverManager..."
        )
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "chrome":
        logger.info(
            "Initiating Driver Instance for Chrome Browser using ChromeDriverManager..."
        )
        return webdriver.Chrome(ChromeDriverManager().install())
    else:
        raise ValueError('value for browser should be either of "chrome" or "firefox"')
