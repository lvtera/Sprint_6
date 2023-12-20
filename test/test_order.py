import pytest

from data import TestData

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize('name, surname, address, metro, phone',
                             [TestData.set_1_positive,
                              TestData.set_2_positive])
    def test_order_creation_successful(self, driver, name, surname, address, metro, phone):
        MainPage(driver).click_to_create_order_button()
        OrderPage(driver).create_order(name, surname, address, metro, phone)
        assert OrderPage(driver).check_order_is_successful()

    def test_header_go_to_order_success(self, driver):
        MainPage(driver).click_to_create_order_header_button()
        assert MainPage(driver).check_order_creation_page_opened()
