import allure

from pages.main_page import MainPage


class TestRedirection:

    @allure.title('Переход на главную страницу по клику на лого Самокат в хэдере')
    def test_click_on_scooter_logo_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_create_order_header_button()
        main_page.click_to_scooter_logo()
        assert main_page.check_main_page_order_button_text() == 'Заказать', ("Главная страница Яндекс.Самокат не "
                                                                             "открылась")

    @allure.title('Переход на страницу Дзен по клику на лого Яндекс в хэдере')
    def test_click_on_dzen_logo_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_dzen_logo()
        main_page.switch_to_new_window()
        assert main_page.check_dzen_opened(), "Главная страница Дзен не открылась"
