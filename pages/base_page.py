from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator, parent=None):
        if parent :
            parent.find_element(*locator).click()
        else:
            self.find(locator).click()

    def input_text(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def get_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title