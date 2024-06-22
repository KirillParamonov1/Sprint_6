import allure

from Sprint_6.pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Проверка оформления заказа')
    def test_order_form(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_order_url()
        order_page.first_form_metro()
        order_page.next_button()
        order_page.second_form()
        result = order_page.result()

        assert 'Заказ оформлен' and 'Номер заказа:' in result, 'Не удалось оформить заказ'