import allure
import pytest

from data import TestData

from pages.main_page import MainPage


class TestFaqSection:

    @allure.title('Работа выпадающего списка в разделе Вопросы о важном')
    @pytest.mark.parametrize('question, answer',
                             [TestData.question_1,
                              TestData.question_2,
                              TestData.question_3,
                              TestData.question_4,
                              TestData.question_5,
                              TestData.question_6,
                              TestData.question_7,
                              TestData.question_8
                              ])
    def test_check_faq_items_success(self, driver, question, answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq()
        main_page.click_on_question(question)
        main_page.get_question(question)
        assert main_page.get_answer(question) == answer, "Получен неверный ответ в выпадающем списке"
