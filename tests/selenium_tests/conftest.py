import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def browser():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-dev-shm-usage')

    browser = Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
