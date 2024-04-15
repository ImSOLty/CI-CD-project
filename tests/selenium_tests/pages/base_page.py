import os
from datetime import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .control.js_scripts import JSScript

TEST_RESULTS = os.path.join(os.path.dirname(__file__), '../../test_results/')
SCREENSHOT_FORMAT = "%Y-%m-%d-%H-%M-%S-%f"

class BasePage:
    _browser = None

    def __init__(self, browser: WebDriver, transition_needed=None):
        self._browser = browser
        if transition_needed:
            self._browser.get(transition_needed)

    def take_screenshot(self):
        try:
            os.makedirs(f'{TEST_RESULTS}/selenium_screenshots')
        except FileExistsError:
            pass
        filename = f'{TEST_RESULTS}/selenium_screenshots/{datetime.utcnow().strftime(SCREENSHOT_FORMAT)}.png'
        print('Taken screenshot:', filename)
        self._browser.save_screenshot(filename)

    def element_exists(self, locator):
        try:
            self._browser.find_element(locator[0], locator[1])
        except NoSuchElementException:
            return False
        return True

    def find_by_locator(self, locator):
        try:
            elem = self._browser.find_element(locator[0], locator[1])
            self._browser.execute_script(JSScript.SCROLL_INTO_VIEW, elem)
        except NoSuchElementException:
            assert False, f'Element not found, {self._browser.current_url=}, {locator=}'
        return elem

    def find_multiple_by_locator(self, locator):
        return self._browser.find_elements(locator[0], locator[1])

    def remove_elements(self, locator):
        elements = self.find_multiple_by_locator(locator)
        for el in elements:
            self._browser.execute_script(JSScript.REMOVE_ELEMENT, el)

    def wait_until(self, until_action):
        WebDriverWait(self._browser, 10).until(
            until_action
        )

    def wait_url_change(self, action=None):
        prev_url = self._browser.current_url
        if action:
            action()
        self.wait_until(expected_conditions.url_changes(prev_url))

    def wait_element_loaded(self, locator):
        self.wait_until(expected_conditions.element_to_be_clickable(locator))

    def set_implicit_wait(self, seconds):
        self._browser.implicitly_wait(seconds)

    def get_xpath(self, elm):
        e = elm
        xpath = elm.tag_name
        while e.tag_name != "html":
            e = e.find_element(By.XPATH, "..")
            neighbours = e.find_elements(By.XPATH, "../" + e.tag_name)
            level = e.tag_name
            if len(neighbours) > 1:
                level += "[" + str(neighbours.index(e) + 1) + "]"
            xpath = level + "/" + xpath
        return "/" + xpath

    def get_browser(self):
        return self._browser
