import pytest

from selenium import webdriver
from src.config import Config


# @pytest.fixture
@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    # Закомментировать следующие 2 строки для отображения браузера во время тестов
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    driver.quit()
