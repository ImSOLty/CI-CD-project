from selenium.webdriver import ActionChains

from .control.locators import OPOPLocators
from .trajectories_page import TrajectoriesPage


class OpopListPage(TrajectoriesPage):

    def create_new_document(self, study_field, study_plan):
        self.find_by_locator(OPOPLocators.CREATE_NEW_BUTTON).click()
        self.wait_element_loaded(OPOPLocators.CREATE_NEW_FINISH_BUTTON)
        for inp, value in zip(self.find_multiple_by_locator(OPOPLocators.SELECTS_TO_CREATE), [study_field, study_plan]):
            inp.click()
            locator = OPOPLocators.SELECTS_TO_CREATE_OPTION(value)
            option = inp.find_element(locator[0], locator[1])
            option.click()

        self.take_screenshot()
        self.find_by_locator(OPOPLocators.CREATE_NEW_FINISH_BUTTON).click()

    def save_document_url(self):
        self.wait_url_change()
        return self._browser.current_url.split('?')[0]

    def remove_document_with_code(self, code):
        # define document row
        row = self.find_by_locator(OPOPLocators.ROW_WITH_CODE(code)).get_attribute('row-index')
        self.find_by_locator(OPOPLocators.REMOVE_BUTTON_FOR_ROW(row)).click()
        self.wait_element_loaded(OPOPLocators.CONFIRM_DELETE_BUTTON)
        self.find_by_locator(OPOPLocators.CONFIRM_DELETE_BUTTON).click()

