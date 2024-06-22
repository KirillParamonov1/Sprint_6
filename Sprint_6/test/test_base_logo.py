import allure

from Sprint_6.pages.main_page import MainPage


class TestRedirects:
    @allure.title('Проверка перехода на страницу "Дзен" с помощью логотипа "Яндекс"')
    def test_go_to_dzen(self, driver):
        main_page = MainPage(driver)
        ya_url = main_page.go_to_dzen_and_get_url()

        assert 'dzen.ru' in ya_url, 'Не удалось перейти на страницу Дзен'

    @allure.title('Проверка перехода на главную страницу')
    def test_go_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_header_order_button()
        result = main_page.click_to_logo_and_get_content()
        assert "Вопросы о важном" in result