from pages.login_page import LoginPage


def test_successful_login_with_page_object(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url