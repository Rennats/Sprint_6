import allure
import pytest

from conftest import driver
from src.config import Config
from src.pages.main_page import MainPage
from src.pages.order_page import OrderPage


@allure.feature("Test making of order")
class TestOrder:
    order_data = [
        ("Иван", "Иванов", "Москва, ул. Ленина 1", "Сокольники", "+79991234567", "09.09.2025", "сутки", "black", "Комментарий1", "top"),
        ("Петр", "Петров", "Москва, ул. Пушкина 2", "Черкизовская", "+79997654321", "02.10.2025", "двое суток", "grey", "Комментарий2", "bottom")
        ]

    @allure.title("Order scooter from {entry_point}")
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, period, color, comment, entry_point", order_data)
    def test_order_scooter(self, driver, entry_point, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)
        # Обработка запроса на сохранение cookie
        main_page.check_cookie()
        # Обработка точки входа в сценарий заказа самоката: кнопка сверху или снизу страницы
        if entry_point == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

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
        assert driver.current_url == Config.URL

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
        assert "dzen.ru" in driver.current_url
