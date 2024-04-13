import os

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from .actions import TrajectoriesActions
from .data_test import DataTest

LOGIN, PASSWORD = os.getenv('LOGIN'), os.getenv('PASSWORD')


@pytest.mark.selenium_tests
class TestSelenium:

    def test_fill_456(self, browser: WebDriver):
        actions = TrajectoriesActions()
        actions.authorize_lk_etu(browser, LOGIN, PASSWORD)
        actions.auth_as_person_with_id(browser, DataTest.PERSON_ID)
        actions.create_opop(browser)
        actions.edit_opop_document(browser)
        actions.get_document_json(browser)
        actions.check_if_data_is_saved()
        actions.remove_document_with_code(browser, DataTest.STUDY_PLAN.split()[0])
