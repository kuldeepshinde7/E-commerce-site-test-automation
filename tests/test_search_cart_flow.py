from pages.home_page import HomePage
from pages.cart_page import CartPage
from selenium.common.exceptions import TimeoutException


def test_search_non_existing_product(driver, non_existing_term):
    home = HomePage(driver)
    home.search(non_existing_term)
    try:
        text = home.get_no_result_text()
        assert "no results found" in text.lower()
    except TimeoutException:
        assert False, "Expected no-result message but it didn't appear"



def test_search_existing_product(driver, search_term):
    home = HomePage(driver)
    home.search(search_term)
    results = home.get_search_results()
    assert any(search_term.lower() in result.text.lower() for result in results)


def test_add_to_cart(driver, product_index):
    cart = CartPage(driver)
    cart.add_to_cart_by_index(product_index)
    cart.open_cart()
    assert cart.get_cart_item_count() == 1


def test_update_quantity(driver, product_index, quantity):
    cart = CartPage(driver)
    cart.add_to_cart_by_index(product_index)
    cart.open_cart()
    cart.update_quantity(quantity)



def test_remove_product(driver, product_index):
    cart = CartPage(driver)
    cart.add_to_cart_by_index(product_index)
    cart.open_cart()
    cart.remove_item()
    assert cart.get_cart_item_count() == 0

