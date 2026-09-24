from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_complete_purchase(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    assert cart_page.get_item_name() == "Sauce Labs Backpack"

    cart_page.start_checkout()

    checkout_page.enter_customer_information(
        "Nevena",
        "Suknovic",
        "11000"
    )

    checkout_page.finish_order()

    assert checkout_page.get_complete_message() == (
        "Thank you for your order!"
    )