import allure
import pytest

from Sprint_6.data import DataAnswer, DataOrder
from Sprint_6.locators.main_page_locators import MainPageLocators
from Sprint_6.pages.main_page import MainPage
from Sprint_6.pages.order_page import OrderPage


class TestForMainPage:
    @allure.title('Тестирование открытия выбранного вопроса и сравнение с ожидаемым ответом')
    @pytest.mark.parametrize('question, answer, true_answer',
                             [(MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, DataAnswer.ANSWER_Q_1),
                              (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, DataAnswer.ANSWER_Q_2),
                              (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, DataAnswer.ANSWER_Q_3),
                              (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, DataAnswer.ANSWER_Q_4),
                              (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, DataAnswer.ANSWER_Q_5),
                              (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, DataAnswer.ANSWER_Q_6),
                              (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, DataAnswer.ANSWER_Q_7),
                              (MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_8, DataAnswer.ANSWER_Q_8)])
    def test_question(self, question, answer, true_answer, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_question_block()
        main_page.click_to_question_for_get_answer(question)
        text_answer = main_page.get_text_from_element(answer)
        assert text_answer == true_answer


    @allure.title('Проверка перехода на страницу оформления заказа')
    @pytest.mark.parametrize(
        "order_locators",
        [MainPageLocators.ORDER_BUTTON_HEADER,
         MainPageLocators.ORDER_BUTTON_MIDDLE]
    )
    def test_order_button(self, driver, order_locators):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.scroll_to_order_button_and_click(order_locators)
        result = order_page.get_content_title()
        expected_result = DataOrder.ORDER_TITLE

        assert result == expected_result, 'Не удалось перейти на страницу оформления заказа'