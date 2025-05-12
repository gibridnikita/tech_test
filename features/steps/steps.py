from behave import given, when, then

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@given('user navigates to "{url}"')
def page_navigation(context, url):
    LoginPage(context.driver).get_login_page(url)


@when('user logins with "{username}" login and "{password}" password')
def page_login(context, username, password):
    LoginPage(context.driver).login(username, password)


@when('user presses "{label}" button under "{product_name}" product')
def manage_cart(context, label, product_name):
    InventoryPage(context.driver).click_product_button(product_name, label)


@then('user should see "{text}" in the page title')
def verify_page_title(context, text):
    actual_title = LoginPage(context.driver).get_page_title()
    expected_title = text
    assert actual_title == expected_title, f"Page title mismatch. Expected: {expected_title}, but got: {actual_title}"


@then('user should see "{text}" page header')
def verify_page_header(context, text):
    actual_header = InventoryPage(context.driver).get_page_header()
    expected_header = text
    assert actual_header == expected_header, f"Page header mismatch. Expected: {expected_header}, but got: {actual_header}"


@then('user should see "{count}" items in inventory table')
def verify_inventory_count(context, count):
    actual_count = InventoryPage(context.driver).get_inventory_count()
    expected_count = int(count)
    assert actual_count == expected_count, f"Inventory count mismatch. Expected: {expected_count}, but got: {actual_count}"


@then('user should see "{count}" item(s) in shopping cart')
def verify_shopping_cart_count(context, count):
    actual_count = InventoryPage(context.driver).get_cart_counter()
    assert actual_count == count, f"Shopping cart count mismatch. Expected: {count}, but got: {actual_count}"
