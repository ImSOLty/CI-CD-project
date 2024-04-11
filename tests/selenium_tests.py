import os
from datetime import datetime

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

TEST_RESULTS = os.path.dirname(__file__) + '/test_results'


@pytest.fixture(scope='session')
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    browser = Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield browser
    browser.quit()


def take_screenshot(browser):
    try:
        os.makedirs(f'{TEST_RESULTS}/selenium_screenshots')
    except FileExistsError:
        pass
    filename = f'{TEST_RESULTS}/selenium_screenshots/{datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S-%f")}.png'
    print('Taken screenshot:', filename)
    browser.save_screenshot(filename)


@pytest.mark.selenium_tests
class TestSelenium:
    def test_something(self, browser):
        browser.get('https://python.org')
        take_screenshot(browser)
