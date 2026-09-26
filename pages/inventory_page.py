from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    BACKPACK_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'inventory_item')]"
        "[.//*[normalize-space()='Sauce Labs Backpack']]"
        "//button[normalize-space()='Add to cart']",
    )
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BACKPACK_BUTTON)
        ).click()

    def get_cart_count(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text

    def open_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()