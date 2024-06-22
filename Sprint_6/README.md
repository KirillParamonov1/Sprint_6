# Sprint_6
Автоматизированные тесты для проверки сервиса заказа самокатов: https://qa-scooter.praktikum-services.ru/

Директория проекта:
* allure_results - директория с отчетами allure
* locators - директория локаторов 
  * main_page_locators.py - локаторы главной страницы 
  * order_page_locators.py - локаторы страницы заказа
* pages - директория методов страниц
  * base_page.py - общие методы 
  * main_page.py - методы для главной страницы 
  * order_page.py - методы для страницы заказа
* tests - директория тестов 
  * test_main_page.py - тесты для главной страницы 
  * test_order_page.py - тесты для страницы заказа
* conftest.py - фикстуры
* data.py - данные для параметризации
* README.md - описание проекта
* requirements - файл с внешними зависимостями
* settings - файл с используемыми URL