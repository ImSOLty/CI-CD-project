import re
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from .pages.trajectories_page import TrajectoriesPage
from .pages.etu_auth_page import EtuAuthPage
from .pages.admin_fake_page import AdminFakePage
from .pages.opop_list_page import OpopListPage
from .pages.document_page import DocumentPage

from .pages.control.urls import Urls
from .data_test import DataTest


class TrajectoriesActions:
    _content = None
    _json_data = None

    def authorize_lk_etu(self, browser: WebDriver, login, password):
        traj_page = TrajectoriesPage(browser, Urls.TRAJECTORIES)
        traj_page.take_screenshot()
        traj_page.remove_modal_if_exists()
        traj_page.accept_cookies()
        traj_page.enter_by_etu()

        etu_lk_page = EtuAuthPage(traj_page.get_browser())
        etu_lk_page.take_screenshot()

        etu_lk_page.authorize_by_form(login, password)

        # Auth trajectories with ETU ID:
        # the first for linking etu id with etu lk
        # the second for linking trajectories and etu lk)
        traj_page = TrajectoriesPage(browser, Urls.TRAJECTORIES)
        traj_page.remove_modal_if_exists()
        traj_page.enter_by_etu()
        etu_lk_page = EtuAuthPage(traj_page.get_browser())
        etu_lk_page.wait_lk_loaded()
        etu_lk_page.take_screenshot()
        traj_page = TrajectoriesPage(browser, Urls.TRAJECTORIES)
        traj_page.remove_modal_if_exists()
        traj_page.enter_by_etu()
        # etu_lk_page = EtuAuthPage(traj_page.get_browser(), transition_needed=False)
        # etu_lk_page.authorize_by_form(LOGIN, PASSWORD)

    def auth_as_person_with_id(self, browser: WebDriver, person_id: int):
        adm_page = AdminFakePage(browser, Urls.ADMIN_FAKE)
        adm_page.remove_modal_if_exists()
        adm_page.take_screenshot()
        adm_page.auth_as_person(person_id)

    def create_opop(self, browser: WebDriver):
        opop_list_page = OpopListPage(browser, Urls.OPOP_LIST)
        opop_list_page.remove_modal_if_exists()
        opop_list_page.take_screenshot()
        opop_list_page.create_new_document(DataTest.STUDY_FIELD, DataTest.STUDY_PLAN)
        opop_list_page.take_screenshot()
        Urls.DOCUMENT_PAGE = opop_list_page.save_document_url()
        print(Urls.DOCUMENT_PAGE)

    def edit_opop_document(self, browser: WebDriver):
        document_page = DocumentPage(browser, Urls.DOCUMENT_PAGE)
        document_page.remove_modal_if_exists()
        document_page.wait_loading()
        document_page.take_screenshot()
        document_page.set_implicit_wait(1)
        self._content = document_page.fill_sections()
        document_page.take_screenshot()
        document_page.set_implicit_wait(10)
        document_page.save_document()
        document_page.take_screenshot()

    def get_document_json(self, browser: WebDriver):
        document_page = DocumentPage(browser, Urls.DOCUMENT_PAGE)
        document_page.remove_modal_if_exists()
        document_page.wait_loading()
        document_page.take_screenshot()
        self._json_data = document_page.get_document_in_json()
        # print(self._json_data)
        document_page.take_screenshot()

    def check_if_data_is_saved(self):
        def get_value_by_json_pointer(pointer, data_json):
            current = data_json
            for field in pointer.split('/'):
                current = current[int(field) if field.isnumeric() else field]
            return current

        for value, mapping in DataTest.MAPPING_DATA_TO_JSON.items():
            value = self._content[value]
            if isinstance(mapping, str):
                expected = get_value_by_json_pointer(mapping, self._json_data)
                assert value.strip() in expected, f'Incorrect value for {mapping}. Expected: {expected}. Got: {value}'
            else:
                for additional, val in zip(['code', 'value'], re.split(r'\.? ', value, 1)):
                    expected = get_value_by_json_pointer(mapping[additional], self._json_data)
                    assert val.strip() in expected, f'Incorrect value for {mapping}. Expected: {expected}. Got: {val}'

    def remove_document_with_code(self, browser: WebDriver, code: str):
        opop_list_page = OpopListPage(browser, Urls.OPOP_LIST)
        opop_list_page.remove_modal_if_exists()
        opop_list_page.take_screenshot()
        opop_list_page.remove_document_with_code(code)
        opop_list_page.take_screenshot()
