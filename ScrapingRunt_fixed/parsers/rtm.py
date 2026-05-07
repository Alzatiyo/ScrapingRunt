from selenium.webdriver.common.by import By


def parse_rtm(driver):
    """
    Extrae los datos de la Revisión Técnico-Mecánica desde la tabla #tablaRTM.
    Retorna dict vacío si no hay datos o la tabla no existe.
    """

    rows = driver.find_elements(By.CSS_SELECTOR, "#tablaRTM tr")

    if len(rows) < 2:
        return {}

    cols = rows[1].find_elements(By.TAG_NAME, "td")

    if len(cols) < 3:
        return {}

    return {
        "rtm_cda": cols[0].text.strip(),
        "rtm_fecha": cols[1].text.strip(),
        "rtm_vencimiento": cols[2].text.strip()
    }
