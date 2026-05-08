from selenium.webdriver.common.by import By
from extract.extraer_tabla_mat import extraer_tabla_mat

def extraer_soat(driver):
    soat = None
    try:
        panel = driver.find_element(
            By.XPATH, "//cyrconsultavehiculo-poliza-soat//mat-card-content")

        if panel.find_elements(By.XPATH, ".//*[contains(text(),'No se encontró')]"):
            print("  SOAT: Sin información.")
            return soat

        # A: mat-table
        soat_lista = extraer_tabla_mat(panel)

        if soat_lista:
            soat = soat_lista[0]   # ← SOLO EL PRIMERO

        # B: label/b rows
        if not soat:
            registro = {}
            for fila in panel.find_elements(By.XPATH, ".//div[contains(@class,'row')]"):
                for lbl, bold in zip(
                    fila.find_elements(By.TAG_NAME, "label"),
                    fila.find_elements(By.TAG_NAME, "b")
                ):
                    k = lbl.text.strip().rstrip(":")
                    v = bold.text.strip()
                    if k and v:
                        registro[k] = v

            if registro:
                soat = registro

        # C: texto plano
        if not soat:
            texto = panel.text.strip()
            if texto and "No se encontró" not in texto:
                soat = {"texto_raw": texto}

        if soat:
            print("  SOAT: registro encontrado.")
        else:
            print("  SOAT: sin datos.")

    except Exception as e:
        print(f"  [ERROR] extrayendo SOAT: {e}")

    return soat