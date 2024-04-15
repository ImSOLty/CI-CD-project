import json
import os

import time
import random
from tkinter import Tk

from selenium.common import NoSuchElementException

from .trajectories_page import TrajectoriesPage
from .control.locators import DocumentPageLocators
from .control.js_scripts import JSScript


def generate_random_numeric(n=2):
    return ''.join(str(random.randint(1, 9)) for _ in range(n))


class DocumentPage(TrajectoriesPage):
    result = dict()

    def save_to_result(self, upper_tab_num, left_tab_num, elem):
        self.result[(upper_tab_num, left_tab_num, self.get_xpath(elem))] = elem.text

    def fill_sections(self):
        upper_tabs = self.find_multiple_by_locator(DocumentPageLocators.UPPER_TABS)
        for upper_tab_num in [2, 4, 5]:
            # including 2nd because it is necessary for the 4th
            # excluding 6th because there are no fields to fill
            self._browser.execute_script(JSScript.SCROLL_TO_TOP)
            upper_tabs[upper_tab_num].click()
            for left_tab_num, left_tab in enumerate(self.find_multiple_by_locator(DocumentPageLocators.LEFT_TABS)):
                left_tab.click()
                self.fill_section(upper_tab_num, left_tab_num)
                time.sleep(0.5)
        return self.result

    def wait_loading(self):
        self.wait_element_loaded(DocumentPageLocators.TABS_INCLUDED)

    def fill_section(self, upper_tab_num, left_tab_num):
        for i, ms_field in enumerate(self.find_multiple_by_locator(DocumentPageLocators.MULTISELECT_FIELDS)):
            ms_field.click()
            options = self.find_multiple_by_locator(DocumentPageLocators.MULTISELECT_FIELDS_OPTION)
            if len(options) > 0:
                self.result[f'{upper_tab_num},{left_tab_num},multiselect,{i}'] = options[0].text

                options[0].click()
        for i, textarea_field in enumerate(self.find_multiple_by_locator(DocumentPageLocators.TEXTAREA_FIELDS)):
            value = generate_random_numeric()
            textarea_field.send_keys(value)
            self.result[f'{upper_tab_num},{left_tab_num},textarea_field,{i}'] = value
        for i, input_field in enumerate(self.find_multiple_by_locator(DocumentPageLocators.INPUT_FIELDS)):
            value = generate_random_numeric()
            input_field.send_keys(value)
            self.result[f'{upper_tab_num},{left_tab_num},input_field,{i}'] = value
        for i, card_field in enumerate(self.find_multiple_by_locator(DocumentPageLocators.CARDS_FIELDS)):
            self.fill_card(upper_tab_num, left_tab_num, card_field, i)

    def fill_card(self, upper_tab_num, left_tab_num, card_field, card_id):
        try:
            locator = DocumentPageLocators.CARDS_ADD_BUTTON
            card_field.find_element(locator[0], locator[1]).click()
        except NoSuchElementException:
            pass

        k = 0
        while True:
            locator = DocumentPageLocators.UNKNOWN_INPUT_VXE
            for elem in filter(lambda el: len(el.text) == 0 or el.text.isspace(),
                               card_field.find_elements(locator[0], locator[1])):

                elem.click()
                options = self.find_multiple_by_locator(DocumentPageLocators.MULTISELECT_FIELDS_OPTION)
                if len(options) > 0:
                    self.result[f'{upper_tab_num},{left_tab_num},card,{card_id},{k}'] = options[0].text
                    options[0].click()
                else:
                    value = generate_random_numeric()
                    try:
                        locator = DocumentPageLocators.INPUT_FIELDS
                        elem.find_element(locator[0], locator[1]).send_keys(value)
                    except NoSuchElementException:
                        locator = DocumentPageLocators.TEXTAREA_FIELDS
                        elem.find_element(locator[0], locator[1]).send_keys(value)
                    self.result[f'{upper_tab_num},{left_tab_num},card,{card_id},{k}'] = value

            # search for expanding button
            locator = DocumentPageLocators.LAST_EXPANDING_BUTTON
            exp_buttons = card_field.find_elements(locator[0], locator[1])
            locator = DocumentPageLocators.TABLE_ROWS_INSIDE_CARD
            total_rows = card_field.find_elements(locator[0], locator[1])

            if len(exp_buttons) == 0 or len(total_rows) > len(exp_buttons) + 1:
                return
            self._browser.execute_script(JSScript.SCROLL_INTO_VIEW, exp_buttons[-1])
            exp_buttons[-1].click()

            k += 1

    def save_document(self):
        self.find_by_locator(DocumentPageLocators.SAVE_DOCUMENT_BUTTON).click()
        self.wait_element_loaded(DocumentPageLocators.SAVED_INFO)

    def get_document_in_json(self):
        self.find_by_locator(DocumentPageLocators.JSON_LINK).click()
        self._browser.execute_script(JSScript.SCROLL_TO_TOP)
        self.wait_element_loaded(DocumentPageLocators.JSON_COPY_BUTTON)
        self.find_by_locator(DocumentPageLocators.JSON_COPY_BUTTON).click()
        self.wait_element_loaded(DocumentPageLocators.JSON_COPIED_RESPONSE)

        if os.environ.get('DISPLAY', '') == '':
            print('no display found. Using :0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')

        return json.loads(Tk().clipboard_get().replace('\n', ''))
