from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_CONSENT = (By.XPATH, "//div[contains(@class,'App_CookieConsent')]")
    COOKIE_BTN = (By.ID, "rcc-confirm-button")
    DZEN_STELLA = (By.XPATH, "//div[contains(@class,'stella_logo')]")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[contains(@class,'Button_Button')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")

class OrderPageLocators:
    NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    SURNAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")
    PHONE_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.CSS_SELECTOR, ".Dropdown-placeholder")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class,'Order_Modal')]")
    SUCCESS_TEXT = (By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")