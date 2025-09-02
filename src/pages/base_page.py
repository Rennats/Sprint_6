from allure import step
from src.config import Config
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    def find_element(self, locator):
        with step(f"Find element {locator}"):
            return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        with step(f"Click to {locator}"):
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        with step(f"Fill text '{text}' into field {locator}"):
            self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        with step(f"Get text of {locator}"):
            return self.find_element(locator).text


    def is_displayed(self, locator):
        with step(f"Check the visibility of {locator}"):
            return self.find_element(locator).is_displayed()

    def element_is_present(self, locator):
        with step(f"Check the presence of {locator}"):
            try:
                self.wait.until(EC.presence_of_element_located(locator))
                return True
            except TimeoutException:
                return False

    def scroll_to_element(self, locator):
        with step(f"Scroll to element {locator}"):
            # Скролл до нужного пункта FAQ
            self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(locator))
            self.wait.until(EC.visibility_of_element_located(locator))

    def switch_to_last_window(self):
        with step("Switch to last browser window"):
            self.driver.switch_to.window(self.driver.window_handles[-1])
