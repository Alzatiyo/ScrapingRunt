from selenium.webdriver.common.by import By
from extract._normalizar_rtm import _normalizar_rtm
from extract.extraer_tabla_mat import extraer_tabla_mat


def extraer_rtm(driver):
    """
    Columnas reales de la mat-table RTM en RUNT:
      numeCerti | fechaExpedicion | fechaVigencia | nombreCda | informacionConsistente | vigente
    """
    rtm = None
    try:
        panel = driver.find_element(
            By.XPATH, "//cyrconsultavehiculo-rtm//mat-card-content")

        if panel.find_elements(By.XPATH, ".//*[contains(text(),'No se encontró')]"):
            print("  RTM: Sin información.")
            return rtm

        # A: mat-table
        rtm_lista = extraer_tabla_mat(panel)

        if rtm_lista:
            rtm = rtm_lista[0]   # ← SOLO EL PRIMERO

        # B: mat-card por certificado
        if not rtm:
            for tarjeta in panel.find_elements(By.XPATH, ".//mat-card"):
                registro = {}
                for elem in tarjeta.find_elements(By.XPATH, ".//p | .//div"):
                    try:
                        strong = elem.find_elements(By.TAG_NAME, "strong")
                        if not strong:
                            continue

                        clave = strong[0].text.strip().rstrip(":")
                        valor = elem.text.replace(strong[0].text, "").strip().lstrip(":").strip()

                        if clave:
                            registro[clave] = valor

                    except:
                        pass

                if registro:
                    rtm = registro
                    break

        # B2: label/b rows
        if not rtm:
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
                rtm = registro

        # C: texto plano
        if not rtm:
            texto = panel.text.strip()
            if texto and "No se encontró" not in texto:
                rtm = {"texto_raw": texto}

        if rtm:
            rtm = _normalizar_rtm(rtm)

        if rtm:
            print("  RTM: registro encontrado.")
        else:
            print("  RTM: sin datos.")

    except Exception as e:
        print(f"  [ERROR] extrayendo RTM: {e}")

    return rtm