from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_backpack_with_page_object(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"