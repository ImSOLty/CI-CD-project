import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def browser():
    browser = Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    browser.quit()


@pytest.mark.selenium_tests
class TestSelenium:
    def test_something(self, browser):
        assert True
