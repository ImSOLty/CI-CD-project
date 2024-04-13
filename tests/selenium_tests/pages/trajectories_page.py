from .base_page import BasePage
from .control.locators import TrajectoriesLocators, AuthEtuLocators


class TrajectoriesPage(BasePage):
    def remove_modal_if_exists(self):
        if self.element_exists(TrajectoriesLocators.NAV_BAR):
            self.remove_elements(TrajectoriesLocators.NAV_BAR)
        if self.element_exists(TrajectoriesLocators.DEV_SERVER_MODAL):
            self.remove_elements(TrajectoriesLocators.DEV_SERVER_MODAL)

    def enter_by_etu(self):
        self.wait_url_change(self.find_by_locator(TrajectoriesLocators.ENTER_VIA_ETU_ID).click)
        # Go to ETU ID
        self.wait_url_change(self.find_by_locator(AuthEtuLocators.SUBMIT_BUTTON).click)

    def accept_cookies(self):
        if self.element_exists(TrajectoriesLocators.ACCEPT_COOKIES):
            self.find_by_locator(TrajectoriesLocators.ACCEPT_COOKIES).click()


