from selenium.webdriver.common.by import By


def parse_info_general(driver):
    """
    Extrae los datos de la tabla de información general del vehículo.
    Busca específicamente la tabla de info general para no mezclar
    datos del SOAT o RTM.
    """

    data = {}

    # Buscar tablas que NO sean la de SOAT ni RTM
    tables = driver.find_elements(By.CSS_SELECTOR, "table")

    for table in tables:
        # Saltar tablas de SOAT y RTM que tienen sus propios parsers
        table_id = table.get_attribute("id") or ""
        if "SOAT" in table_id or "RTM" in table_id:
            continue

        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")

            if len(cols) == 2:
                key = cols[0].text.strip()
                val = cols[1].text.strip()

                if key:
                    data[key] = val

    return data
