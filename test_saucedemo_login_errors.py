import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        (
            "invalid_user",
            "wrong_password",
            "Username and password do not match"
        ),
        (
            "",
            "secret_sauce",
            "Username is required"
        ),
        (
            "standard_user",
            "",
            "Password is required"
        )
    ]
)

def test_login_error_messages(
    driver,
    username,
    password,
    expected_message
):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.ID, "user-name"
    ).send_keys(username)

    driver.find_element(
        By.ID, "password"
    ).send_keys(password)

    driver.find_element(
        By.ID, "login-button"
    ).click()
    
    wait = WebDriverWait(driver, 10)
    

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert expected_message in error_message.text