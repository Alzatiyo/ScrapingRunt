from selenium.webdriver.common.by import By


def parse_result(driver):

    data = {}

    rows = driver.find_elements(By.CSS_SELECTOR,"#tablaVehiculo tr")

    for r in rows:

        cols = r.find_elements(By.TAG_NAME,"td")

        if len(cols)==2:

            data[cols[0].text] = cols[1].text


    soat_rows = driver.find_elements(By.CSS_SELECTOR,"#tablaSoat tr")

    if len(soat_rows)>1:

        cols = soat_rows[1].find_elements(By.TAG_NAME,"td")

        data["soat_poliza"] = cols[0].text
        data["soat_inicio"] = cols[1].text
        data["soat_fin"] = cols[2].text


    rtm_rows = driver.find_elements(By.CSS_SELECTOR,"#tablaRtm tr")

    if len(rtm_rows)>1:

        cols = rtm_rows[1].find_elements(By.TAG_NAME,"td")

        data["rtm_cda"] = cols[0].text
        data["rtm_vencimiento"] = cols[1].text

    return data