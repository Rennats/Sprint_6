from allure import step
from src.locators.locators import MainPageLocators
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    _FAQ_ACCORDION_HEADING_XPATH = "//div[(@id='accordion__heading-{}')]"
    _FAQ_ACCORDION_PANEL_XPATH = "//div[(@id='accordion__panel-{}')]//p"

    def __init__(self, driver):
        super().__init__(driver)

    def check_cookie(self):
        # Обработка запроса на сохранение cookie
        if self.element_is_present(MainPageLocators.COOKIE_CONSENT):
            with step(f"Click to allow cookies button"):
                self.click_element(MainPageLocators.COOKIE_BTN)

    def click_order_button_top(self):
        with step("Click to top order button"):
            self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        with step("Click to bottom order button"):
            self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_faq_question(self, index):
        # Динамическое создание локатора FAQ_ACCORDION_HEADING
        faq_accordion_heading_locator = (By.XPATH, self._FAQ_ACCORDION_HEADING_XPATH.format(index))
        # Скролл до нужного пункта FAQ
        self.scroll_to_element(faq_accordion_heading_locator)
        # Проверка отображения нужного пункта FAQ
        self.element_is_present(faq_accordion_heading_locator)
        # Нажатие на нужный пункт FAQ
        self.click_element(faq_accordion_heading_locator)
        # Динамическое создание локатора FAQ_ACCORDION_PANEL
        faq_accordion_panel_locator = (By.XPATH, self._FAQ_ACCORDION_PANEL_XPATH.format(index))
        # Ожидание отображения текста FAQ
        self.element_is_present(faq_accordion_panel_locator)

    def get_faq_answer(self, index):
        # Динамическое создание локатора FAQ_ACCORDION_PANEL
        faq_accordion_panel_locator = (By.XPATH, self._FAQ_ACCORDION_PANEL_XPATH.format(index))
        return self.get_text(faq_accordion_panel_locator)

    def check_click_scooter_logo(self):
        with step("Click to scooter logo"):
            self.click_element(MainPageLocators.SCOOTER_LOGO)

    def check_click_yandex_logo(self):
        with step("Click to Yandex logo"):
            self.click_element(MainPageLocators.YANDEX_LOGO)

    def check_dzen_stella(self):
        return self.element_is_present(MainPageLocators.DZEN_STELLA)
