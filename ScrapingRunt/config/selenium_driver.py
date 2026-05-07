from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.user_agents import random_agent


def crear_driver():

    options = Options()

    options.add_argument(f"user-agent={random_agent()}")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    return driver