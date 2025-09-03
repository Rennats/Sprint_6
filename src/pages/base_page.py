import allure

from src.config import Config
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    @allure.step("BasePage class initialization")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    @allure.step("Find element {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Click to element {locator}")
    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Fill text '{text}' into field {locator}")
    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Get text of element {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Check the visibility of element {locator}")
    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    @allure.step("Check the presence of element {locator}")
    def element_is_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Scroll to element {locator}")
    def scroll_to_element(self, locator):
        # Скролл до нужного пункта FAQ
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(locator))
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Switch to last browser window")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Get the current page url")
    def get_current_url(self):
        return self.driver.current_url
