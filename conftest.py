import os
import re

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def driver(request):
    options = Options()

    # Isključuje Google Password Manager popup
    options.add_argument(
        "--disable-features=PasswordLeakDetection"
    )
    options.add_argument("--disable-notifications")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )

    # Opcije potrebne za GitHub Actions
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser

    # Proverava da li je test pao
    test_result = getattr(
        request.node,
        "rep_call",
        None
    )

    # Automatski pravi screenshot neuspešnog testa
    if test_result and test_result.failed:
        os.makedirs(
            "artifacts",
            exist_ok=True
        )

        safe_test_name = re.sub(
            r"[^a-zA-Z0-9_-]",
            "_",
            request.node.name
        )

        screenshot_path = (
            f"artifacts/FAILED_{safe_test_name}.png"
        )

        browser.save_screenshot(screenshot_path)

    browser.quit()


@pytest.fixture
def api_client():
    session = requests.Session()

    session.headers.update(
        {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )

    yield session

    session.close()