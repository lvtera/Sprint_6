from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = By.XPATH, "//input[contains(@placeholder, 'Имя')]"
    SURNAME_FIELD = By.XPATH, "//input[contains(@placeholder, 'Фамилия')]"
    ADDRESS_FIELD = By.XPATH, "//input[contains(@placeholder, 'Адрес')]"
    METRO_STATION_FIELD = By.XPATH, "//input[contains(@placeholder, 'Станция метро')]"
    METRO_STATION_LIST = By.XPATH, "//ul/li/button/div[text()='{}']"
    TEL_NUMBER_FIELD = By.XPATH, "//input[contains(@placeholder, 'Телефон')]"
    CONTINUE_BUTTON = By.XPATH, "//*[contains(@class, 'Order_NextButton')]/button"
    DELIVERY_DATE_FIELD = By.XPATH, "//input[contains(@placeholder, 'Когда привезти')]"
    DELIVERY_DATE_CALENDAR = By.XPATH, "//div[contains(@class, 'today')]/following-sibling::div[1]"
    RENT_DURATION_FIELD = By.XPATH, "//div[@class='Dropdown-control']"
    RENT_DURATION_LIST_ITEM = By.XPATH, "//div[text()='сутки']"
    ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"
    CONFIRM_ORDER_BUTTON = By.XPATH, "//button[text()='Да']"
    ORDER_SUCCESSFUL_MODAL_WINDOW_TEXT = By.XPATH, "//*[text()='Заказ оформлен']"
