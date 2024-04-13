from .base_page import BasePage
from .control.locators import AuthEtuLocators


class EtuAuthPage(BasePage):

    def authorize_by_form(self, login, password):

        if self.element_exists(AuthEtuLocators.PASSWORD_FIELD):
            self.find_by_locator(AuthEtuLocators.EMAIL_FIELD).send_keys(login)
            self.find_by_locator(AuthEtuLocators.PASSWORD_FIELD).send_keys(password)
            if self.element_exists(AuthEtuLocators.REMEMBER_CHECKBOX):
                self.find_by_locator(AuthEtuLocators.REMEMBER_CHECKBOX).click()

        self.wait_url_change(self.find_by_locator(AuthEtuLocators.SUBMIT_BUTTON).click)

    def wait_lk_loaded(self):
        self.wait_element_loaded(AuthEtuLocators.LK_STUDENT_BODY_ID)
