from selenium.webdriver.common.by import By

PARENT_NODE = (By.XPATH, "./..")
PARENT_NODE_WITH_TAG = lambda tag: (By.XPATH, f"/ancestor::{tag}")


class AuthEtuLocators:
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    REMEMBER_CHECKBOX = (By.ID, "remember")
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    LOGOUT_LINK = (By.XPATH, '//a[contains(@href="logout")]')
    LK_STUDENT_BODY_ID = (By.ID, 'body-clone')


class TrajectoriesLocators:
    NAV_BAR = (By.TAG_NAME, 'nav')
    DEV_SERVER_MODAL = (By.ID, "devServerModalId___BV_modal_outer_")
    ENTER_VIA_ETU_ID = (By.XPATH, '//button[contains(text(), "ETU ID")]')
    ACCEPT_COOKIES = (By.XPATH, '//*[@data-cy = "cookies-ok-button"]')


class AdminFakeLocators:
    PERSON_ID = lambda x: (
        By.XPATH, f'//div[@ref="eCenterContainer"]//div[@col-id="id"]//span[contains(text(),\"{x}\")]')
    NEXT_PAGE = (By.XPATH, '//button[contains(text(),"Next")]')
    FROM_ID, TO_ID = (By.XPATH, '//*[@ref="lbFirstRowOnPage"]'), (By.XPATH, '//*[@ref="lbLastRowOnPage"]')


class OPOPLocators:
    CREATE_NEW_BUTTON = (By.CSS_SELECTOR, '.row button:nth-of-type(1)')
    SELECTS_TO_CREATE = (By.CSS_SELECTOR, '.multiselect')
    SELECTS_TO_CREATE_OPTION = lambda x: (By.XPATH, f'//*[contains(text(),"{x}")]')
    CREATE_NEW_FINISH_BUTTON = (
        By.XPATH, '//div[@id="creationModalId___BV_modal_content_"]//button[contains(text(),"Добавить")]'
    )
    DISABLED_OPTIONS = (By.CSS_SELECTOR, '.multiselect__option--disabled')

    ROW_WITH_CODE = lambda code: (By.XPATH, f'//span[text()="{code}"]/ancestor::div[@role="row"]')
    REMOVE_BUTTON_FOR_ROW = lambda row_id: (
        By.XPATH, f'//div[@class="ag-pinned-right-cols-container"]//div[@role="row" and @row-index={row_id}]//button[2]'
    )
    CONFIRM_DELETE_BUTTON = (By.XPATH, '//div[@id="deleteModal"]//button[contains(text(), "Удалить")]')
    DELETED_INFO = (By.XPATH, '//*[text()="Удаление выбранного ОПОП выполнено"]')


class DocumentPageLocators:
    TABS_INCLUDED = (By.XPATH, '//ul[@role="tablist" and contains(@class,"nav-tabs")]')
    UPPER_TABS = (By.XPATH, '//ul[@role="tablist" and contains(@class,"nav-tabs")]//li[@role="presentation"]')
    LEFT_TABS = (By.XPATH, '//div[@class="tab-content"]//li[@role="presentation"]')

    MULTISELECT_FIELDS = (By.CSS_SELECTOR, '.field-multiselect .multiselect')
    MULTISELECT_TAG = (By.CSS_SELECTOR, '.multiselect__tag')
    MULTISELECT_FIELDS_OPTION = (
        By.XPATH,
        './/div[contains(@class,"multiselect--active")]//span[contains(@class,"multiselect__option--highlight")]'
    )

    TEXTAREA_FIELDS = (By.XPATH, './/textarea[not(@readonly)]')
    INPUT_FIELDS = (By.XPATH, './/input[@type and not(@class="multiselect__input")]')

    CARDS_FIELDS = (By.XPATH, './/*[@class="card-body" and not(@role)]')
    CARDS_ADD_BUTTON = (By.XPATH, './/button/span[contains(text(),"Добавить")]')
    UNKNOWN_INPUT_VXE = (By.XPATH, './/*[@class="vxe-tree-cell" or @class="vxe-cell--label"]/ancestor::td')
    LAST_EXPANDING_BUTTON = (By.XPATH, './/button[@title="Добавить на уровень ниже"]')
    TABLE_ROWS_INSIDE_CARD = (By.XPATH, './/tbody//tr')

    SAVE_DOCUMENT_BUTTON = (By.XPATH, '//span[@title="Сохранить документ"]')
    SAVED_INFO = (By.XPATH, '//*[text()="Выполнено сохранение текущего документа ОПОП"]')

    JSON_LINK = (By.XPATH, '//a[contains(text(), "JSON (dev)")]')
    JSON_COPY_BUTTON = (By.XPATH, '//span[contains(text(),"copy")]')
    JSON_COPIED_RESPONSE = (By.XPATH, '//span[contains(text(),"copied")]')
    JSON_CODE_CONTENT = (By.CSS_SELECTOR, '.jv-code.open.boxed')
