"""
cart_page.py

Handles cart operations: add item, update quantity, remove item, get cart status.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart_by_index(self, index):
        add_buttons = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "add-to-cart")))
        if index < len(add_buttons):
            add_buttons[index].click()
        else:
            raise IndexError("Product index out of range.")

    def open_cart(self):
        cart_button = self.wait.until(EC.element_to_be_clickable((By.ID, "cart-button")))
        cart_button.click()

    def update_quantity(self, quantity):
        qty_input = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-quantity")))
        qty_input.clear()
        qty_input.send_keys(str(quantity))
        update_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "update-cart")))
        update_btn.click()

    def remove_item(self):
        remove_btn = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "remove-from-cart")))
        remove_btn.click()

    def get_cart_item_count(self):
        try:
            count_text = self.wait.until(EC.presence_of_element_located((By.ID, "cart-count"))).text
            return int(count_text) if count_text.strip().isdigit() else 0
        except:
            return 0

    def get_cart_total_price(self):
        try:
            total = self.wait.until(EC.presence_of_element_located((By.ID, "cart-total"))).text
            return float(total.replace("₹", "").strip()) if total else 0.0
        except:
            return 0.0