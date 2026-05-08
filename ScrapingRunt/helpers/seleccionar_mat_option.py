from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def seleccionar_mat_option(driver, texto, timeout=10):

    opciones = WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "mat-option .mat-option-text")))

    for op in opciones:
        if texto.lower() in op.text.strip().lower():
            op.click()
            return op.text.strip()

    opciones[0].click()
    return opciones[0].text.strip()