import pytest
from selenium import webdriver
from data import Urls
from locators.main_page_locators import MainPageLocators


@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--window-size=1280,800')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(Urls.MAIN_PAGE_URL)
    driver.find_element(*MainPageLocators.ALLOW_COOKIE_BUTTON).click()
    yield driver
    driver.quit()
