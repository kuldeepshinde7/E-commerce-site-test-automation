from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "search-input")
        self.search_button = (By.ID, "search-button")
        self.results = (By.CLASS_NAME, "product-title")
        self.no_result = (By.ID, "no-result-message")

    def search(self, keyword):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_box)
        ).clear()
        self.driver.find_element(*self.search_box).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def get_search_results(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.results)
        )

    def get_no_result_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.no_result)
        ).text
