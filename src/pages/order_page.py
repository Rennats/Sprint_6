import allure

from src.locators.locators import OrderPageLocators
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    @allure.step("OrderPage class initialization")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Update locator {locator} with data {data}")
    def _update_select_data_locator(self, locator, data):
        # Обновление данных элемента локатора
        locator_list = list(locator)
        locator_list[1] = locator_list[1].format(data)
        return tuple(locator_list)

    @allure.step("Fill order personal info")
    def fill_personal_info(self, name, surname, address, metro, phone):
        self.enter_text(OrderPageLocators.NAME_FIELD, name)
        self.enter_text(OrderPageLocators.SURNAME_FIELD, surname)
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_element(OrderPageLocators.METRO_FIELD)
        # Динамическое создание локатора выбора станции метро
        metro_locator = self._update_select_data_locator(OrderPageLocators.COMBO_BOX_DATA_OPTION, metro)
        self.click_element(metro_locator)
        self.enter_text(OrderPageLocators.PHONE_FIELD, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Fill order rental info")
    def fill_rental_info(self, date, period, color, comment):
        self.enter_text(OrderPageLocators.DATE_FIELD, date)
        # Выбор цвета
        color_locator = getattr(OrderPageLocators, color)
        self.click_element(color_locator)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        # Динамическое создание локатора выбора срока аренды
        period_locator = self._update_select_data_locator(OrderPageLocators.COMBO_BOX_DATA_OPTION, period)
        self.click_element(period_locator)
        self.enter_text(OrderPageLocators.COMMENT_FIELD, comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Placing order via confirm button")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Check that success order modal window is displayed")
    def is_success_modal_displayed(self):
        return self.is_displayed(OrderPageLocators.SUCCESS_MODAL)

    @allure.step("Get success placing of order text")
    def get_success_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_TEXT)