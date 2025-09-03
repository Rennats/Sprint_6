import allure
import pytest

from src.pages.main_page import MainPage
from src.data import faq_data

@allure.feature("Check FAQ answers")
class TestFAQ:

    @allure.title("Check FAQ answer № {index}: ")
    @pytest.mark.parametrize("index, expected_answer", faq_data)
    def test_faq_answer(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        # Обработка запроса на сохранение cookie
        main_page.check_cookie()
        # Проверка соответствия текста при нажатии на вопрос FAQ
        main_page.click_faq_question(index)
        assert main_page.get_faq_answer(index) == expected_answer
