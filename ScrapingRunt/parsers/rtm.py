from selenium.webdriver.common.by import By


def parse_rtm(driver):

    rows = driver.find_elements(By.CSS_SELECTOR, "#tablaRTM tr")

    if len(rows) < 2:
        return {}

    cols = rows[1].find_elements(By.TAG_NAME, "td")

    return {

        "rtm_cda": cols[0].text,
        "rtm_fecha": cols[1].text,
        "rtm_vencimiento": cols[2].text
    }