import allure

from allure import step
from src.locators.locators import MainPageLocators
from src.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("MainPage class initialization")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Update locator {locator} for FAQ item №{index}")
    def _update_locator_index(self, locator, index):
        # Обновление индекса элемента локатора
        locator_list = list(locator)
        locator_list[1] = locator_list[1].format(index)
        return tuple(locator_list)

    @allure.step("Proceed allow cookie request")
    def check_cookie(self):
        # Обработка запроса на сохранение cookie
        if self.element_is_present(MainPageLocators.COOKIE_CONSENT):
            with step(f"Click to allow cookies button"):
                self.click_element(MainPageLocators.COOKIE_BTN)

    @allure.step("Click make order button at top of main page")
    def click_order_button_top(self):
        with step("Click to top order button"):
            self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Click make order button at bottom of main page")
    def click_order_button_bottom(self):
        with step("Click to bottom order button"):
            self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Click FAQ question item №{index}")
    def click_faq_question(self, index):
        # Обновление локатора FAQ_ACCORDION_HEADING
        faq_accordion_heading_locator = self._update_locator_index(MainPageLocators.FAQ_ACCORDION_HEADING, index)
        # Скролл до нужного пункта FAQ
        self.scroll_to_element(faq_accordion_heading_locator)
        # Проверка отображения нужного пункта FAQ
        self.element_is_present(faq_accordion_heading_locator)
        # Нажатие на нужный пункт FAQ
        self.click_element(faq_accordion_heading_locator)
        # Обновление локатора FAQ_ACCORDION_PANEL
        faq_accordion_panel_locator = self._update_locator_index(MainPageLocators.FAQ_ACCORDION_PANEL, index)
        # Ожидание отображения текста нужного пункта FAQ
        self.element_is_present(faq_accordion_panel_locator)

    @allure.step("Get text of FAQ question item №{index}")
    def get_faq_answer(self, index):
        # Обновление локатора FAQ_ACCORDION_PANEL
        faq_accordion_panel_locator = self._update_locator_index(MainPageLocators.FAQ_ACCORDION_PANEL, index)
        return self.get_text(faq_accordion_panel_locator)

    @allure.step("Click to scooter logo on main page")
    def check_click_scooter_logo(self):
        with step("Click to scooter logo"):
            self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Click to Yandex logo on main page")
    def check_click_yandex_logo(self):
        with step("Click to Yandex logo"):
            self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Check presence of Dzen stella logo on main page")
    def check_dzen_stella(self):
        return self.element_is_present(MainPageLocators.DZEN_STELLA)
