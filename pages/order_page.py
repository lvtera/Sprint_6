import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнение поля Имя")
    def set_name(self, text):
        self.send_text_to_field(OrderPageLocators.NAME_FIELD, text)

    @allure.step("Заполнение поля Фамилия")
    def set_surname(self, text):
        self.send_text_to_field(OrderPageLocators.SURNAME_FIELD, text)

    @allure.step("Заполнение поля Адрес")
    def set_address(self, text):
        self.send_text_to_field(OrderPageLocators.ADDRESS_FIELD, text)

    @allure.step("Выбор станции метро")
    def set_metro_station(self, text):
        self.send_text_to_field(OrderPageLocators.METRO_STATION_FIELD, text)
        method, locator = OrderPageLocators.METRO_STATION_LIST
        locator = locator.format(text)
        self.click_to_element((method, locator))

    @allure.step("Заполнение поля Телефон")
    def set_tel_number(self, text):
        self.send_text_to_field(OrderPageLocators.TEL_NUMBER_FIELD, text)

    @allure.step("Клик по конпке Далее")
    def click_to_continue_button(self):
        self.click_to_element(OrderPageLocators.CONTINUE_BUTTON)

    @allure.step("Выбор даты доставки самоката")
    def set_delivery_date(self):
        self.click_to_element(OrderPageLocators.DELIVERY_DATE_FIELD)
        self.click_to_element(OrderPageLocators.DELIVERY_DATE_CALENDAR)

    @allure.step("Выбор срока аренды")
    def set_rent_duration(self):
        self.click_to_element(OrderPageLocators.RENT_DURATION_FIELD)
        self.click_to_element(OrderPageLocators.RENT_DURATION_LIST_ITEM)

    @allure.step("Сделать заказ кликом на кнопку Заказать")
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Клик по кнопке Да для подтверждения заказа")
    def click_to_confirm_order_button(self):
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Проверка успешного создания заказа")
    def check_order_is_successful(self):
        return self.find_my_element(OrderPageLocators.ORDER_SUCCESSFUL_MODAL_WINDOW_TEXT)

    def create_order(self, name, surname, address, metro, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station(metro)
        self.set_tel_number(phone)
        self.click_to_continue_button()
        self.set_delivery_date()
        self.set_rent_duration()
        self.click_to_order_button()
        self.click_to_confirm_order_button()
