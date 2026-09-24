from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        first_name_field = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        first_name_field.send_keys(first_name)

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last_name)

        self.driver.find_element(
            *self.POSTAL_CODE
        ).send_keys(postal_code)

        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_button.click()

    def finish_order(self):
        finish_button = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )
        finish_button.click()

    def get_complete_message(self):
        complete_message = self.wait.until(
            EC.visibility_of_element_located(
                self.COMPLETE_MESSAGE
            )
        )

        return complete_message.text