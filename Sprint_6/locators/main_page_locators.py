from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, './/div[@id="accordion__heading-{}"]'
    QUESTION_BLOCK = By.XPATH, './/div[@id="accordion__heading-7"]'
    ANSWER_LOCATOR = By.XPATH, './/div[@aria-labelledby="accordion__heading-{}"]'
    ORDER_BUTTON_HEADER = By.XPATH, './/button[@class = "Button_Button__ra12g"]'
    ORDER_BUTTON_MIDDLE = By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]'
    MAIN_PAGE_TITLE = By.XPATH, './/div[@class = "Home_Header__iJKdX"]'
    LOGO_YANDEX = By.XPATH, './/a[@href="//yandex.ru"]'
    CLOSE_DZEN = By.XPATH, './/span[@tabindex = "0"]'
    QUESTIONS = By.XPATH, './/div[text() = "Вопросы о важном"]'
    # первый вопрос
    QUESTION_1 = By.XPATH, './/div[@id="accordion__heading-0"]'
    # второй вопрос
    QUESTION_2 = By.XPATH, './/div[@id="accordion__heading-1"]'
    # третий вопрос
    QUESTION_3 = By.XPATH, './/div[@id="accordion__heading-2"]'
    # четвертый вопрос
    QUESTION_4 = By.XPATH, './/div[@id="accordion__heading-3"]'
    # пятый вопрос
    QUESTION_5 = By.XPATH, './/div[@id="accordion__heading-4"]'
    # шестой вопрос
    QUESTION_6 = By.XPATH, './/div[@id="accordion__heading-5"]'
    # седьмой вопрос
    QUESTION_7 = By.XPATH, './/div[@id="accordion__heading-6"]'
    # восьмой вопрос
    QUESTION_8 = By.XPATH, './/div[@id="accordion__heading-7"]'

    # первый ответ
    ANSWER_1 = By.XPATH, './/div[@id="accordion__panel-0"]'
    # второй ответ
    ANSWER_2 = By.XPATH, './/div[@id="accordion__panel-1"]'
    # третий ответ
    ANSWER_3 = By.XPATH, './/div[@id="accordion__panel-2"]'
    # четвертый ответ
    ANSWER_4 = By.XPATH, './/div[@id="accordion__panel-3"]'
    # пятый ответ
    ANSWER_5 = By.XPATH, './/div[@id="accordion__panel-4"]'
    # шестой ответ
    ANSWER_6 = By.XPATH, './/div[@id="accordion__panel-5"]'
    # седьмой ответ
    ANSWER_7 = By.XPATH, './/div[@id="accordion__panel-6"]'
    # восьмой ответ
    ANSWER_8 = By.XPATH, './/div[@id="accordion__panel-7"]'

    SCOOTER_LOGO = By.XPATH, './/a[@class = "Header_LogoScooter__3lsAR"]'