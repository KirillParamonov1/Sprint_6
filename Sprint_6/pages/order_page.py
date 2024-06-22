import allure

import Sprint_6.settings
from Sprint_6.locators.order_page_locators import OrderPageLocators
from Sprint_6.pages.base_page import BasePage
from Sprint_6.data import DataOrderForm


class OrderPage(BasePage):
    order_url = Sprint_6.settings.order_URL

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step(f"Переход на страницу оформления заказа {order_url}")
    def go_to_order_url(self):
        self.driver.get(self.order_url)


    @allure.step('Открытие формы "Метро" и выбор станции')
    def get_metro(self, locator_metro, locator_station):
        self.click_on_element(locator_metro)
        self.click_on_element(locator_station)

    @allure.step('Заполнение поля "Дата"')
    def set_text_to_date_form(self, date_locator, date):
        self.set_text_to_element(date_locator, date)

    @allure.step("Выбор цвета")
    def choice_of_color(self, color_locator):
        self.click_on_element(color_locator)

    @allure.step("Выбор периода аренды")
    def period_of_time(self, combox_locator, period_locator):
        self.click_on_element(combox_locator)
        self.click_on_element(period_locator)

    @allure.step("Нажатие на кнопку Далее")
    def next_button(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step(
        'Клик на кнопку "Заказать", "Да" и получение текста с окна поддверждения'
    )
    def click_on_order_button_and_get_text_of_notification_window(
            self, order_locator, button_yes_locator, confirm_locator
    ):
        self.click_on_element(order_locator)
        self.click_on_element(button_yes_locator)
        return self.get_text_from_element(confirm_locator)


    @allure.step("Получение текста заголовка страницы создания заказа")
    def get_content_title(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_PAGE_TITLE)

    @allure.step("Переход на страницу создания заказа")
    def go_to_order_page(self):
        self.driver.get(Sprint_6.settings.main_URL + 'order')

    @allure.step("Получение окна с номером заказа")
    def is_order_processed_text_visible(self):
        return 'Заказ оформлен' in self.get_text_from_element(OrderPageLocators.WINDOW)

    @allure.step("Пролистывание до кнопки заказа")
    def order_button_scroll(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_SCROLL)

    @allure.step("Ожидание возможности клика на кнопку заказа и клик по ней")
    def order_button(self):
        self.wait_until_clickable(OrderPageLocators.BUTTON_ORDER)
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step("Заполнение первой формы")
    def first_form_metro(self):
        self.set_text_to_element(OrderPageLocators.PHONE_NUMBER, DataOrderForm.number)
        self.set_text_to_element(OrderPageLocators.NAME, DataOrderForm.name)
        self.set_text_to_element(OrderPageLocators.SURNAME, DataOrderForm.surname)
        self.set_text_to_element(OrderPageLocators.ADDRESS, DataOrderForm.street)
        self.set_text_to_element(OrderPageLocators.PHONE_NUMBER, DataOrderForm.number)
        self.get_metro(OrderPageLocators.METRO, OrderPageLocators.METRO_STATION_1)


    @allure.step("Заполнение второй формы")
    def second_form(self):

        self.set_text_to_date_form(OrderPageLocators.DATE, DataOrderForm.date_1)
        self.click_on_element(OrderPageLocators.BLACK_COLOR)
        self.period_of_time(OrderPageLocators.RENT_PERIOD, OrderPageLocators.THREE_DAYS)

    @allure.step("Нажатие на кнопки заказа")
    def result(self):
        self.find_element_with_wait(OrderPageLocators.BUTTON_ORDER)
        self.order_button_scroll()
        self.order_button()
        self.click_on_order_button_and_get_text_of_notification_window(OrderPageLocators.YES_BUTTON)
        self.click_on_order_button_and_get_text_of_notification_window(OrderPageLocators.CONFIRM)

        period_choice = self.find_element_with_wait(OrderPageLocators.THREE_DAYS)
        period_choice.click()

        color = self.find_element_with_wait(OrderPageLocators.GREY_COLOR)
        color.click()

        self.click_on_element(OrderPageLocators.BUTTON_ORDER)
        self.click_on_element(OrderPageLocators.YES_BUTTON)