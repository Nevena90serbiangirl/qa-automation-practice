from decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait


def test_prices_sorted_low_to_high(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        lambda browser: browser.find_elements(
            By.CLASS_NAME, "inventory_item_price"
        )
    )

    sort_menu = Select(
        driver.find_element(By.CLASS_NAME, "product_sort_container")
    )
    sort_menu.select_by_value("lohi")

    prices = [
        Decimal(item.text.replace("$", ""))
        for item in driver.find_elements(
            By.CLASS_NAME, "inventory_item_price"
        )
    ]

    assert len(prices) > 1
    assert prices == sorted(prices)