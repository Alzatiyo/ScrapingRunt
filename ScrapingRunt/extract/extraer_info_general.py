from selenium.webdriver.common.by import By


def extraer_info_general(driver):
    """
    Zona 1 — panel-content  rows: pares label / b
              → PLACA, Nro. licencia, Estado, Tipo de servicio, Clase de vehículo

    Zona 2 — mat-card  p <strong>campo:</strong> valor
              → Marca, Línea, Modelo, Color, Nro. motor, Chasis, VIN, etc.
    """
    datos = {}

    # ── Zona 1 ───────────────────────────────────────────────────────────────
    try:
        filas = driver.find_elements(
            By.XPATH,
            "//cyrconsultavehiculo-info-vehiculo-detallada"
            "//div[contains(@class,'panel-content')]"
            "//div[contains(@class,'row')]"
        )
        for fila in filas:
            labels = fila.find_elements(By.TAG_NAME, "label")
            bolds  = fila.find_elements(By.TAG_NAME, "b")
            for lbl, bold in zip(labels, bolds):
                k = lbl.text.strip().rstrip(":")
                v = bold.text.strip()
                if k and v:
                    datos[k] = v
    except Exception as e:
        print(f"  [WARN] info general zona 1: {e}")

    # ── Zona 2 ───────────────────────────────────────────────────────────────
    try:
        parrafos = driver.find_elements(
            By.XPATH,
            "//cyrconsultavehiculo-info-vehiculo-detallada//mat-card//p"
        )
        for p in parrafos:
            try:
                strong = p.find_elements(By.TAG_NAME, "strong")
                if not strong:
                    continue
                clave = strong[0].text.strip().rstrip(":")
                # valor = texto del <p> menos el texto del <strong>
                valor = p.text.strip().replace(strong[0].text, "").strip().lstrip(":").strip()
                if clave:
                    datos[clave] = valor        # guarda aunque valor esté vacío
            except Exception:
                pass
    except Exception as e:
        print(f"  [WARN] info general zona 2: {e}")

    return datos