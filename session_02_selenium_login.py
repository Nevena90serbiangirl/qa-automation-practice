from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    actual_heading = driver.find_element(By.CLASS_NAME, "title").text
    expected_heading = "Products"

    assert actual_heading == expected_heading, (
        f"Expected '{expected_heading}', "
        f"but received '{actual_heading}'"
    )

    print("PASSED: User logged in successfully.")

finally:
    driver.quit()