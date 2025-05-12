from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_HEADER = (By.CSS_SELECTOR, ".title")
    INVENTORY_TABLE = (By.ID, "inventory_container")
    SHOPPING_CART = (By.ID, "shopping_cart_container")
    INVENTORY_ITEM_DESCRIPTION = ".//div[text() = '{}']/ancestor::div[@class = 'inventory_item_description']"

    def __init__(self, driver):
        super().__init__(driver)
        self.inventory_table = self.find(self.INVENTORY_TABLE)

    def get_page_header(self):
        return self.get_text(self.PAGE_HEADER)

    def get_inventory_count(self):
        inventory_items = self.inventory_table.find_elements(By.CSS_SELECTOR, ".inventory_item")
        inventory_items_count = len(inventory_items)
        return inventory_items_count

    def get_inventory_item(self, product_name):
        return self.inventory_table.find_element(By.XPATH, self.INVENTORY_ITEM_DESCRIPTION.format(product_name))

    def click_product_button(self, product_name, label):
        button_locator = (By.XPATH, f".//button[. = '{label}']")
        product_item = self.get_inventory_item(product_name)
        self.click_element(parent=product_item, locator=button_locator)

    def get_cart_counter(self):
        return self.get_text(self.SHOPPING_CART)
