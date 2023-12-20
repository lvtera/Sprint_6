from pages.main_page import MainPage


class TestRedirection:

    def test_click_on_scooter_logo_success(self, driver):
        MainPage(driver).click_to_create_order_header_button()
        MainPage(driver).click_to_scooter_logo()
        assert MainPage(driver).check_main_page_order_button_text() == 'Заказать'

    def test_click_on_dzen_logo_success(self, driver):
        MainPage(driver).click_to_dzen_logo()
        MainPage(driver).switch_to_new_window()
        assert MainPage(driver).check_dzen_opened()
