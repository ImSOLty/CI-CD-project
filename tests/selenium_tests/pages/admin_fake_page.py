from selenium.webdriver import ActionChains

from .control.locators import AdminFakeLocators
from .trajectories_page import TrajectoriesPage


class AdminFakePage(TrajectoriesPage):

    def find_person_on_the_page(self, person_id: int):
        return self.find_by_locator(AdminFakeLocators.PERSON_ID(person_id))

    def go_to_next_page(self):
        self.find_by_locator(AdminFakeLocators.NEXT_PAGE).click()

    def auth_as_person(self, person_id):
        self.take_screenshot()
        fr_id, to_id = (self.find_by_locator(AdminFakeLocators.FROM_ID),
                        self.find_by_locator(AdminFakeLocators.TO_ID))
        while not (int(fr_id.text.replace(',', '')) <= person_id <= int(to_id.text.replace(',', ''))):
            self.go_to_next_page()
            fr_id, to_id = (self.find_by_locator(AdminFakeLocators.FROM_ID),
                            self.find_by_locator(AdminFakeLocators.TO_ID))
        element = self.find_person_on_the_page(person_id)
        self.take_screenshot()
        ActionChains(self._browser).double_click(element).perform()
