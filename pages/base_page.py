# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))