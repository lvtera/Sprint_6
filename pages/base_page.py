from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_my_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def send_text_to_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
