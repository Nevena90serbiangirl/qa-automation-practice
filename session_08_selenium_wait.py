from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    
    driver.find_element(
        By.ID, "user-name"
    ).send_keys("standard_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID, "login-button"
    ).click()
    
    wait = WebDriverWait(driver, 10)

    heading = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    assert heading.text == "Products"

    print("PASSED: Products heading is visible.")

finally:
    
    driver.quit()