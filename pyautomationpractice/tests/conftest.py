import typing

import pytest
from selenium import webdriver

from pyautomationpractice import logger
from pyautomationpractice.utilities import get_driver_for_browser


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="Chrome",
        help="browser: Provide Browser Name for Test. Supports Chrome and Firefox",
    )
    parser.addoption(
        "--implicitWait",
        action="store",
        default="60",
        help="implicit wait value.",
    )
    parser.addoption(
        "--username",
        action="store",
        default="",
        help="Username to Log In..",
    )
    parser.addoption(
        "--password",
        action="store",
        default="",
        help="Password to Log In..",
    )


@pytest.fixture(scope="session")
def pyf_base_url() -> str:
    return "http://www.automationpractice.com"


@pytest.fixture(scope="session")
def pyf_implicit_wait(request) -> int:
    return int(request.config.getoption("--implicitWait"))


@pytest.fixture(scope="session")
def pyf_username(request) -> str:
    username = request.config.getoption("--username")
    logger.info(f"Username User-Defined Value from CLI option: {username}")
    return username


@pytest.fixture(scope="session")
def pyf_password(request) -> str:
    password = request.config.getoption("--password")
    logger.info(f"Password User-Defined Value from CLI option: {password}")
    return password

@pytest.fixture(scope="session")
def pyf_browser_name(request) -> str:
    browser = request.config.getoption("--browser")
    logger.info(f"Browser User-Defined Value from CLI option: {browser}")
    return browser


@pytest.fixture
def pyf_driver(
    pyf_browser_name: str,
) -> typing.Union[webdriver.Firefox, webdriver.Chrome]:
    return get_driver_for_browser(pyf_browser_name)


@pytest.fixture(autouse=True)
def case_setup(
    request,
    pyf_driver: typing.Union[webdriver.Firefox, webdriver.Chrome],
    pyf_base_url: str,
    pyf_implicit_wait: int,
):
    pyf_driver.implicitly_wait(pyf_implicit_wait)
    pyf_driver.maximize_window()
    pyf_driver.get(pyf_base_url)

    def teardown():
        logger.info("Quitting WebDriver...")
        pyf_driver.quit()

    request.addfinalizer(teardown)