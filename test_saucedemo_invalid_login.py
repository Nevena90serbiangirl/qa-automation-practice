

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



    
    
def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.ID, "user-name"
    ).send_keys("invalid_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("wrong_password")

    driver.find_element(
        By.ID, "login-button"
    ).click()
    
    wait = WebDriverWait(driver, 10)

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "Username and password do not match" in error_message.text