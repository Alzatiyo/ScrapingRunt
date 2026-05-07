from scraper.runt_scraper import consultar_runt
from config.selenium_driver import crear_driver

from parsers.info_general import parse_info_general
from parsers.soat import parse_soat
from parsers.rtm import parse_rtm


def process_vehicle(item):

    driver = crear_driver()

    placa = item["placa"]
    documento = item["documento"]

    try:

        consultar_runt(driver, placa, documento)

        data = {
            **parse_info_general(driver),
            **parse_soat(driver),
            **parse_rtm(driver),
            "placa": placa,
            "estado": "OK"
        }

    except Exception as e:

        data = {
            "placa": placa,
            "estado": "ERROR",
            "error": str(e)
        }

    finally:
        driver.quit()

    return data
