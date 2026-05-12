import time
import base64
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.click import click
from helpers.escribir import escribir
from helpers.seleccionar_mat_option import seleccionar_mat_option
from captcha.resolver_captcha import resolver_captcha
from panels.expandir_todos_los_paneles import expandir_todos_los_paneles
from config.settings import URL
from db.actualizar_registro_runt import actualizar_registro_runt


def consultar(driver, placa, documento, tipodoc):
    wait = WebDriverWait(driver, 20)

    if driver.current_url != URL:
        driver.get(URL)
    else:
        driver.refresh()

    wait.until(EC.presence_of_element_located((By.ID, "mat-input-0")))
    time.sleep(1)

    print("[1/6] Placa...")
    time.sleep(random.uniform(0.3,0.8))
    escribir(driver, By.ID, "mat-input-0", placa)
    time.sleep(0.4)

    print("[2/6] Tipo documento...")
    time.sleep(random.uniform(0.3,0.8))
    click(driver, By.ID, "mat-select-4")
    time.sleep(0.8)


    match tipodoc:        
        case "C.C.":
            seleccionar_mat_option(driver, "Cédula Ciudadanía")
        case "C.E.":
            seleccionar_mat_option(driver, "Cédula de Extranjería")
        case "NIT":
            seleccionar_mat_option(driver, "NIT")
        case "P.":
            seleccionar_mat_option(driver, "Pasaporte")
        case "P.P.T.":
            seleccionar_mat_option(driver, "Permiso por Protección Temporal")
        case "R.C.":
            seleccionar_mat_option(driver, "Registro Civil")
        case "T.I.":
            seleccionar_mat_option(driver, "Tarjeta de Identidad")
        case _:
            seleccionar_mat_option(driver, "Cédula Ciudadanía")

    time.sleep(0.4)

    print("[3/6] Número documento...")
    time.sleep(random.uniform(0.3,0.8))
    escribir(driver, By.ID, "mat-input-1", documento)
    time.sleep(0.4)

    for intento in range(3):
        print(f"[4/6] Captcha (intento {intento+1}/3)...")
        img = wait.until(EC.presence_of_element_located((
            By.XPATH,
            "//img[contains(@src,'data:image') and contains(@class,'img-responsive')]"
        )))
        time.sleep(0.5)
        src = img.get_attribute("src") or ""
        if src.startswith("data:image"):
            _, b64 = src.split(",", 1)
            img_bytes = base64.b64decode(b64)
        else:
            img_bytes = img.screenshot_as_png

        texto_captcha = resolver_captcha(img_bytes)
        if not texto_captcha:
            print("anticaptcha no devolvió solución")
            continue

        campo = driver.find_element(By.ID, "mat-input-2")
        campo.clear()
        campo.send_keys(texto_captcha)
        driver.execute_script("""
            arguments[0].focus();
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input'));
            arguments[0].dispatchEvent(new Event('change'));
        """, campo, texto_captcha)
        time.sleep(0.3)

        time.sleep(random.uniform(1.2,2))
        print("[5/6] Click Consultar...")
        btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@type='submit' and contains(.,'Consultar')]"
        )))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        time.sleep(0.3)
        btn.click()

        print("[6/6] Esperando resultados...")
        time.sleep(1)

        popup = driver.find_elements(By.CLASS_NAME, "swal2-container")

        if popup:
            print("Popup detectado (datos incorrectos). Saltando placa...")
            actualizar_registro_runt(placa)

            try:
                driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
            except:
                pass

            return None

        en_formulario = driver.find_elements(By.ID, "mat-input-0")
        if not en_formulario:
            break
        print("Captcha incorrecto, reintentando...")
        time.sleep(1)   

    expandir_todos_los_paneles(driver)
    time.sleep(2)

    return driver.page_source