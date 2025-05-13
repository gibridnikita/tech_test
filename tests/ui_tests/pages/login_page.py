from selenium.webdriver.common.by import By
from tests.ui_tests.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PAGE_HEADER = (By.CSS_SELECTOR, ".title")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page(self,url):
        self.get_page(url)

    def get_page_title(self):
        return self.get_title()

    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)