from selenium.webdriver.common.by import By


def parse_soat(driver):
    """
    Extrae los datos del SOAT desde la tabla #tablaSOAT.
    Retorna dict vacío si no hay datos o la tabla no existe.
    """

    rows = driver.find_elements(By.CSS_SELECTOR, "#tablaSOAT tr")

    if len(rows) < 2:
        return {}

    cols = rows[1].find_elements(By.TAG_NAME, "td")

    if len(cols) < 4:
        return {}

    return {
        "soat_poliza": cols[0].text.strip(),
        "soat_aseguradora": cols[1].text.strip(),
        "soat_inicio": cols[2].text.strip(),
        "soat_fin": cols[3].text.strip()
    }
