from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASELINE = (
    Path(__file__).parent
    / "portfolio-evidence"
    / "visual-regression"
    / "baseline"
    / "saucedemo-login.png"
)

BASELINE.parent.mkdir(parents=True, exist_ok=True)

if BASELINE.exists():
    print(f"Baseline already exists: {BASELINE}")
else:
    driver = webdriver.Chrome()

    try:
        driver.set_window_size(1280, 800)
        driver.get("https://www.saucedemo.com/")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        )

        driver.save_screenshot(str(BASELINE))
        print(f"Baseline saved: {BASELINE}")
    finally:
        driver.quit()