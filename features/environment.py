import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--incognito")
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.quit()


def before_step(context, step):
    print(f"-> Start step: {step.name}")


def after_step(context, step):
    time.sleep(1)
    print(f"<- End step: {step.name}")
