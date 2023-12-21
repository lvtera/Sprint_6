from selenium.webdriver.common.by import By


class MainPageLocators:
    ALLOW_COOKIE_BUTTON = By.ID, "rcc-confirm-button"
    MAIN_PAGE_ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'Button_Middle')]"
    FAQ_TEXT = By.XPATH, "//div[text()='Вопросы о важном']"
    QUESTIONS_LIST = By.XPATH, "//div[@id='accordion__heading-{}']"
    ANSWERS_LIST = By.XPATH, "//div[@id='accordion__panel-{}']/p"
    HEADER_ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]"
    HEADER_YANDEX_LOGO = By.XPATH, "//*[contains(@class, 'Header_LogoYandex')]"
    HEADER_SCOOTER_LOGO = By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]"
    DZEN_HEADER = By.ID, 'dzen-header'
