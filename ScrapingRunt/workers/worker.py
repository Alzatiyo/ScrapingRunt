from scraper.runt_flow import consultar
from scraper.parser import parse_result
from config.selenium_driver import create_driver


def process_vehicle(item):

    driver = create_driver()

    placa = item["placa"]
    documento = item["documento"]

    try:

        consultar(driver,placa,documento)

        data = parse_result(driver)

        data["placa"] = placa
        data["estado"] = "OK"

    except Exception as e:

        data = {
            "placa": placa,
            "estado": "ERROR",
            "error": str(e)
        }

    driver.quit()

    return data