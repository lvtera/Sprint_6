import pytest

from data import TestData

from pages.main_page import MainPage


class TestFaqSection:

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
        MainPage(driver).scroll_to_faq()
        MainPage(driver).click_on_question(question)
        MainPage(driver).get_question(question)
        assert MainPage(driver).get_answer(question) == answer
