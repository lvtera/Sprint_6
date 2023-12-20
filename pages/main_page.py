import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Переход на страницу создания заказа c главной страницы")
    def click_to_create_order_button(self):
        self.click_to_element(MainPageLocators.MAIN_PAGE_ORDER_BUTTON)

    @allure.step("Переход на страницу создания заказа из хэдера")
    def click_to_create_order_header_button(self):
        self.click_to_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Проверка открытия страницы создания заказа')
    def check_order_creation_page_opened(self):
        return self.find_my_element(OrderPageLocators.CONTINUE_BUTTON)

    @allure.step("Переход к разделу Вопросы о важном")
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ_TEXT)

    @allure.step("Клик на вопрос")
    def click_on_question(self, num):
        method, locator = MainPageLocators.QUESTIONS_LIST
        locator = locator.format(num)
        self.click_to_element((method, locator))

    @allure.step("Получение вопроса из Вопросов о важном")
    def get_question(self, num):
        method, locator = MainPageLocators.QUESTIONS_LIST
        locator = locator.format(num)
        return self.find_my_element((method, locator)).text

    @allure.step("Получение ответа на вопрос")
    def get_answer(self, num):
        method, locator = MainPageLocators.ANSWERS_LIST
        locator = locator.format(num)
        return self.find_my_element((method, locator)).text

    @allure.step("Клик по лого Самокат")
    def click_to_scooter_logo(self):
        self.click_to_element(MainPageLocators.HEADER_SCOOTER_LOGO)

    @allure.step('Проверка перехода на главную страницу')
    def check_main_page_order_button_text(self):
        return self.find_my_element(MainPageLocators.MAIN_PAGE_ORDER_BUTTON).text

    @allure.step("Клик по логотипу Яндекса")
    def click_to_dzen_logo(self):
        self.click_to_element(MainPageLocators.HEADER_YANDEX_LOGO)

    @allure.step('Проверка открытия страницы "Дзен"')
    def check_dzen_opened(self):
        return self.find_my_element(MainPageLocators.DZEN_HEADER)
