from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

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