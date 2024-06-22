import pytest
from selenium import webdriver
import settings


@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=firefox_options)
    driver.get(settings.main_URL)
    yield driver
    driver.quit()