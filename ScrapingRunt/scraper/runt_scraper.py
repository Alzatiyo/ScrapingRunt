from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless
from config.settings import ANTICAPTCHA_KEY

import time
import random


def crear_driver():

    options = Options()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64)"
    ]

    options.add_argument(f"user-agent={random.choice(user_agents)}")

    driver = webdriver.Chrome(options=options)

    return driver


def resolver_captcha(site_key, url):

    solver = recaptchaV2Proxyless()

    solver.set_verbose(1)
    solver.set_key(ANTICAPTCHA_KEY)
    solver.set_website_url(url)
    solver.set_website_key(site_key)

    g_response = solver.solve_and_return_solution()

    if g_response != 0:
        return g_response

    raise Exception("Error resolviendo captcha")


def consultar_runt(placa, documento):

    driver = crear_driver()

    try:

        driver.get("https://www.runt.com.co/consultaCiudadana/#/consultaVehiculo")

        wait = WebDriverWait(driver, 20)

        # ingresar placa
        input_placa = wait.until(
            EC.presence_of_element_located((By.ID, "numeroPlaca"))
        )

        input_placa.send_keys(placa)

        # documento
        input_doc = driver.find_element(By.ID, "numeroDocumento")
        input_doc.send_keys(documento)

        # resolver captcha
        site_key = driver.find_element(By.CLASS_NAME, "g-recaptcha").get_attribute("data-sitekey")

        captcha = resolver_captcha(
            site_key,
            "https://www.runt.com.co/consultaCiudadana/#/consultaVehiculo"
        )

        driver.execute_script(
            "document.getElementById('g-recaptcha-response').innerHTML = arguments[0]",
            captcha
        )

        # buscar
        boton = driver.find_element(By.XPATH, "//button[contains(text(),'Consultar')]")
        boton.click()

        time.sleep(5)

        datos = {}

        try:
            datos["placa"] = placa
            datos["soat"] = driver.find_element(By.XPATH, "//td[contains(text(),'SOAT')]/following-sibling::td").text
        except:
            datos["soat"] = None

        try:
            datos["rtm"] = driver.find_element(By.XPATH, "//td[contains(text(),'RTM')]/following-sibling::td").text
        except:
            datos["rtm"] = None

        return datos

    finally:
        driver.quit()