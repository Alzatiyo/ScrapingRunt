from selenium.webdriver.common.by import By


def parse_soat(driver):

    rows = driver.find_elements(By.CSS_SELECTOR, "#tablaSOAT tr")

    if len(rows) < 2:
        return {}

    cols = rows[1].find_elements(By.TAG_NAME, "td")

    return {

        "soat_poliza": cols[0].text,
        "soat_aseguradora": cols[1].text,
        "soat_inicio": cols[2].text,
        "soat_fin": cols[3].text
    }