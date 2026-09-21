from pathlib import Path

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


ARTIFACTS_DIR = Path("artifacts")


@pytest.mark.smoke
def test_successful_login_screenshot(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.ID, "user-name"
    ).send_keys("standard_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID, "login-button"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory")
    )

    ARTIFACTS_DIR.mkdir(exist_ok=True)

    screenshot_path = ARTIFACTS_DIR / "successful_login.png"
    screenshot_saved = driver.save_screenshot(str(screenshot_path))

    assert screenshot_saved
    assert screenshot_path.exists()