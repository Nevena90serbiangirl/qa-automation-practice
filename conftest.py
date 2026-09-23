import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser

    browser.quit()
    
import requests


@pytest.fixture
def api_client():
    session = requests.Session()
    session.headers.update({
        "Accept": "application/json"
    })

    yield session

    session.close()