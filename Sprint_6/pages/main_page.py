import allure
from Sprint_6.pages.base_page import BasePage
from Sprint_6.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Скролл до блока с вопросами")
    def scroll_to_question_block(self):
        self.scroll_to_element(MainPageLocators.QUESTION_BLOCK)


    @allure.step("Нажимаем на вопрос и получаем ответ")
    def click_to_question_for_get_answer(self, locator):
        self.click_on_element(locator)


    @allure.step("Сравнение полученного ответа и ожидаемого")
    def check_of_answer_result(self, result, expected_result):
        return result == expected_result

    @allure.step('Нажатие на логотип "Яндекс" и получение url')
    def go_to_dzen_and_get_url(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)
        self.jump_new_tab()
        if self.find_element_with_wait(MainPageLocators.CLOSE_DZEN):
            self.click_on_element(MainPageLocators.CLOSE_DZEN)
        return self.get_url_for_page_for_test

    @allure.step('Скролл до кнопки "Заказать" и клик по кнопке "Заказать"')
    def scroll_to_order_button_and_click(self, locator):
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    @allure.step('Нажатие на кнопку Заказ в верхней части сайта')
    def click_to_header_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Клик по лого "Самокат" и получение текста "Самокат на пару дней"')
    def click_to_logo_and_get_content(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)
        self.scroll_to_element(MainPageLocators.QUESTIONS)
        return self.get_text_from_element(MainPageLocators.QUESTIONS)