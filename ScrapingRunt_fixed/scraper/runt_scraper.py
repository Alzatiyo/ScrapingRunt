from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraper.captcha_solver import resolver_captcha
from config.settings import RUNT_URL, TIMEOUT


def consultar_runt(driver, placa, documento):
    """
    Realiza la consulta en el RUNT usando el driver recibido como parámetro.
    NO crea ni cierra el driver internamente.
    """

    driver.get(RUNT_URL)

    wait = WebDriverWait(driver, TIMEOUT)

    # Ingresar placa
    input_placa = wait.until(
        EC.presence_of_element_located((By.ID, "numeroPlaca"))
    )
    input_placa.clear()
    input_placa.send_keys(placa)

    # Ingresar documento
    input_doc = wait.until(
        EC.presence_of_element_located((By.ID, "numeroDocumento"))
    )
    input_doc.clear()
    input_doc.send_keys(documento)

    # Resolver captcha
    recaptcha_elem = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "g-recaptcha"))
    )
    site_key = recaptcha_elem.get_attribute("data-sitekey")

    captcha_token = resolver_captcha(site_key, RUNT_URL)

    driver.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = arguments[0]",
        captcha_token
    )

    # Hacer clic en Consultar
    boton = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Consultar')]"))
    )
    boton.click()

    # Esperar a que los resultados carguen (tabla visible)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    )
