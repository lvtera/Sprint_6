import pytest
import allure

from data import TestData

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Позитивный сценарий заказа самоката')
    @pytest.mark.parametrize('name, surname, address, metro, phone',
                             [TestData.set_1_positive,
                              TestData.set_2_positive])
    def test_order_creation_successful(self, driver, name, surname, address, metro, phone):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_to_create_order_button()
        order_page.create_order(name, surname, address, metro, phone)
        assert order_page.check_order_is_successful(), "Ошибка при оформлении заказа"

    @allure.title('Переход к форме создания заказа по кнопке в хэдере')
    def test_header_go_to_order_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_create_order_header_button()
        assert main_page.check_order_creation_page_opened(), "Ошибка при переходе к форме создания заказа из хэдера"
