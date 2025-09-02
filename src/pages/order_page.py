from src.locators.locators import OrderPageLocators
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    _OPTION_XPATH = "//div[contains(text(), '{}')]"

    # Заполнение персональных данных
    def fill_personal_info(self, name, surname, address, metro, phone):
        self.enter_text(OrderPageLocators.NAME_FIELD, name)
        self.enter_text(OrderPageLocators.SURNAME_FIELD, surname)
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_element(OrderPageLocators.METRO_FIELD)
        # Динамическое создание локатора выбора станции метро
        metro_locator = (By.XPATH, self._OPTION_XPATH.format(metro))
        self.click_element(metro_locator)
        self.enter_text(OrderPageLocators.PHONE_FIELD, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    # Заполнение данных заказа самоката
    def fill_rental_info(self, date, period, color, comment):
        self.enter_text(OrderPageLocators.DATE_FIELD, date)
        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        # Динамическое создание локатора выбора срока аренды
        period_locator = (By.XPATH, self._OPTION_XPATH.format(period))
        self.click_element(period_locator)
        self.enter_text(OrderPageLocators.COMMENT_FIELD, comment)
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    # Подтверждение размещения заказа
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    def is_success_modal_displayed(self):
        return self.is_displayed(OrderPageLocators.SUCCESS_MODAL)

    def get_success_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_TEXT)