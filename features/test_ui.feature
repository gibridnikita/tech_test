Feature: Login and shopping cart on Inventory page

  Background:
    Given user navigates to "https://www.saucedemo.com"
    Then user should see "Swag Labs" in the page title

  Scenario: User is able to login and see products on Inventory page
    When user logins with "standard_user" login and "secret_sauce" password
    Then user should see "Products" page header
    And user should see "6" items in inventory table

  Scenario: User is able to add products in cart
    When user logins with "standard_user" login and "secret_sauce" password
    And user presses "Add to cart" button under "Sauce Labs Backpack" product
    Then user should see "1" item(s) in shopping cart
