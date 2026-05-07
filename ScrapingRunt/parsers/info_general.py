from selenium.webdriver.common.by import By


def parse_info_general(driver):

    data = {}

    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")

    for r in rows:

        cols = r.find_elements(By.TAG_NAME, "td")

        if len(cols) == 2:

            key = cols[0].text.strip()
            val = cols[1].text.strip()

            data[key] = val

    return data