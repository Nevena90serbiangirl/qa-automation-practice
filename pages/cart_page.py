from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_item_name(self):
        wait = WebDriverWait(
            self.driver,
            10,
            ignored_exceptions=(StaleElementReferenceException,)
        )

        return wait.until(
            lambda driver: driver.find_element(
                *self.ITEM_NAME
            ).text or False
        )

    def start_checkout(self):
        checkout_button = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.CHECKOUT_BUTTON
            )
        )

        checkout_button.click()