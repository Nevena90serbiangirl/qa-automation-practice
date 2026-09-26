from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


CURRENT = (
    Path(__file__).parent
    / "portfolio-evidence"
    / "visual-regression"
    / "current"
    / "saucedemo-login.png"
)

CURRENT.parent.mkdir(parents=True, exist_ok=True)

driver = webdriver.Chrome()

try:
    driver.set_window_size(1280, 800)
    driver.get("https://www.saucedemo.com/")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )

    driver.save_screenshot(str(CURRENT))
    print(f"Current saved: {CURRENT}")
finally:
    driver.quit()