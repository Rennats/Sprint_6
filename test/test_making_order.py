import allure
import pytest

from conftest import driver
from src.config import Config
from src.data import order_data
from src.pages.main_page import MainPage
from src.pages.order_page import OrderPage


@allure.feature("Test making of order")
class TestOrder:

    @allure.title("Order scooter by {click_order_button_function} function")
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, period, color, comment, click_order_button_function", order_data)
    def test_order_scooter(self, driver, name, surname, address, metro, phone, date, period, color, comment, click_order_button_function):
        main_page = MainPage(driver)
        # Обработка запроса на сохранение cookie
        main_page.check_cookie()
        # Вход в сценарий заказа самоката - клик по кнопке вверху/внизу через переданное имя функции
        func = getattr(main_page, click_order_button_function)
        func()

        order_page = OrderPage(driver)
        # Заполнение персональных данных
        order_page.fill_personal_info(name, surname, address, metro, phone)
        # Заполнение данных заказа самоката
        order_page.fill_rental_info(date, period, color, comment)
        order_page.confirm_order()
        assert order_page.is_success_modal_displayed()
        assert "Заказ оформлен" in order_page.get_success_text()

    @allure.title("Check scooter logo redirects to main page")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        # Обработка запроса на сохранение cookie
        main_page.check_cookie()
        # Переход на страницу заказа
        main_page.click_order_button_top()
        # Нажатие на логотип 'Самоката'
        main_page.check_click_scooter_logo()
        # Проверка перехода на главную страницу сервиса
        assert main_page.get_current_url() == Config.URL

    @allure.title("Check Yandex logo redirects to Dzen")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        # Обработка запроса на использование cookie
        main_page.check_cookie()
        # Нажатие на логотип Яндекса
        main_page.check_click_yandex_logo()
        # Переключение на последнее окно браузера
        main_page.switch_to_last_window()
        # Проверка на отображение логотипа Дзен
        main_page.check_dzen_stella()
        # Проверка перехода на dzen.ru
        assert "dzen.ru" in main_page.get_current_url()
