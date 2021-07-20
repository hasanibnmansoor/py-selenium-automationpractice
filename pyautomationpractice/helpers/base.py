import typing
from traceback import print_stack

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..utilities.commands import wait_until
from ..utilities.pkg_log import logger

__all__ = ["BaseDriver"]

locator_map = {
    "css_selector": By.CSS_SELECTOR,
    "xpath": By.XPATH,
    "class_name": By.CLASS_NAME,
    "tag_name": By.TAG_NAME,
    "link_text": By.LINK_TEXT,
    "partial_link_text": By.PARTIAL_LINK_TEXT,
    "name": By.NAME,
    "id": By.ID,
}


class BaseDriver:
    def __init__(self, driver: typing.Union[webdriver.Firefox, webdriver.Chrome]):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def get_element(
        self, locator_identifier: str, locator_type: str = "css_selector"
    ) -> typing.Union[WebElement, None]:
        locator_type = locator_type.lower()
        if locator_type not in locator_map.keys():
            raise ValueError(
                f"Invalid Value Passed to locator_type argument. Valid Values are {locator_map.keys()}"
            )

        try:
            logger.info(
                f"Trying to find element with locator type: {locator_type} and locator identifier: {locator_identifier}"
            )
            return self.driver.find_element(
                locator_map[locator_type], locator_identifier
            )
        except NoSuchElementException:
            logger.error(
                f"Element NOT Found with locator type {locator_type} and locator identifier {locator_identifier}"
            )
            print_stack()
            return None
        except Exception:
            logger.warning(
                f"Something went wrong while trying to find element with locator type {locator_type} and locator identifier {locator_identifier}"
            )
            print_stack()
            return None

    def get_elements(
        self, locator_identifier: str, locator_type: str = "css_selector"
    ) -> typing.List[WebElement]:
        locator_type = locator_type.lower()
        _map = {
            "css_selector": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "name": By.NAME,
        }
        if locator_type not in _map.keys():
            raise ValueError(
                f"Invalid Value Passed to locator_type argument. Valid Values are {_map.keys()}"
            )

        logger.info(
            f"Querying DOM to find elements with locator type {locator_type} and locator identifier {locator_identifier}"
        )
        elements = self.driver.find_elements(_map[locator_type], locator_identifier)
        if elements:
            logger.info(
                f"Returned {len(elements)} elements for locator type {locator_type} and locator identifier {locator_identifier}"
            )
        else:
            logger.warning(
                f"No Elements found for locator type {locator_type} and locator identifier {locator_identifier}"
            )
        return elements

    def click(
        self, locator_identifier: str, locator_type: str = "css_selector"
    ) -> None:
        logger.info(f"Trying to CLICK element: {locator_type}: {locator_identifier}")
        elem = self.get_element(locator_identifier, locator_type)
        if elem is not None:
            elem.click()
        else:
            raise NoSuchElementException(
                msg=f"Element with identifier: {locator_identifier} & type: {locator_type} not found to perform CLICK operation."
            )

    def hover_over(
        self, locator_identifier: str, locator_type: str = "css_selector"
    ) -> None:
        logger.info(f"Hovering over element: {locator_type}: {locator_identifier}")
        self.actions.move_to_element(
            self.get_element(locator_identifier, locator_type)
        ).perform()

    def get_page_title(self) -> str:
        return self.driver.title

    def get_tabs(self):
        return self.driver.window_handles

    def switch_tabs(self, tab_name):
        self.driver.switch_to.window(tab_name)

    def switch_to_last_tab(self):
        tabs = self.get_tabs()
        self.switch_tabs(tabs[-1])

    def get_iframes_in_page(self) -> typing.List[WebElement]:
        return self.get_elements(locator_identifier="iframe", locator_type="tag_name")

    def switch_to_iframe(self, iframe_identifier, iframe_identifier_type: str = "id"):
        iframe = self.get_element(iframe_identifier, iframe_identifier_type)
        self.driver.switch_to.frame(iframe)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def verify_page_title(
        self, title_to_verify: str, poll_for_seconds: int = 60
    ) -> bool:
        wait = WebDriverWait(self.driver, poll_for_seconds)
        try:
            return wait.until(EC.title_is(title_to_verify))
        except TimeoutException:
            logger.error(f"Page with title {title_to_verify} not loaded.")
            return False

    def is_element_visible(
        self,
        locator_identifier: str,
        locator_type: str = "css_selector",
        poll_for_seconds: int = 60,
    ) -> typing.Union[WebElement, None]:
        wait = WebDriverWait(self.driver, poll_for_seconds)
        try:
            return wait.until(
                EC.visibility_of_element_located(
                    (locator_map[locator_type], locator_identifier)
                )
            )
        except TimeoutException:
            logger.error(
                f"Element - {locator_type}:{locator_identifier} not visible on screen after polling for {poll_for_seconds} seconds"
            )
            return None

    def wait_until_clickable_and_click(
        self,
        locator_identifier: str,
        locator_type: str = "css_selector",
        poll_for_seconds: int = 60,
    ):
        wait = WebDriverWait(self.driver, poll_for_seconds)
        try:
            el = wait.until(
                EC.element_to_be_clickable(
                    (locator_map[locator_type], locator_identifier)
                )
            )
            el.click()
        except TimeoutException:
            logger.error(
                f"Element - {locator_type}:{locator_identifier} not clickable after polling for {poll_for_seconds} seconds"
            )

    def return_value_from_script(self, javascript: str):
        logger.info(f"Executing JavaScript: {javascript}")
        return self.driver.execute_script(javascript)

    def _is_page_loaded(self):
        rt = self.return_value_from_script("return document.readyState")
        logger.info(f"Current Page Status: {rt}")
        return rt == "complete"

    def wait_for_page_load_complete(self):
        return wait_until(self._is_page_loaded)

    def save_screenshot_to_file(self, file_path: str) -> typing.Union[str, None]:
        logger.info(f"Saving Screenshot to File: {file_path}")
        ss = self.driver.get_screenshot_as_file(file_path)
        return file_path if ss else None

    def scroll_element_to_view(self, element):
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center",behavior: "smooth",});',
            element,
        )

    def enter_text(
        self, locator_identifier: str, locator_type: str, text_to_be_entered: str
    ):
        input_element = self.is_element_visible(locator_identifier, locator_type)
        assert (
            input_element is not None
        ), f"Element with {locator_type}: {locator_identifier} not visible on screen"
        input_element.send_keys(text_to_be_entered)
