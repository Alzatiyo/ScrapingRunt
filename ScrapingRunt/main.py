from config.database import obtener_placas
from config.selenium_driver import crear_driver

from scraper.runt_scraper import consultar_runt

from parsers.info_general import parse_info_general
from parsers.soat import parse_soat
from parsers.rtm import parse_rtm

from storage.excel_exporter import guardar_excel

import random
import time


def main():

    consultas = obtener_placas()

    print("Placas a consultar:", len(consultas))

    driver = crear_driver()

    resultados = []

    try:

        for item in consultas:

            placa = item["placa"]
            documento = item["documento"]

            print("Consultando:", placa)

            try:

                consultar_runt(driver, placa, documento)

                info = parse_info_general(driver)
                soat = parse_soat(driver)
                rtm = parse_rtm(driver)

                resultados.append({
                    "placa": placa,
                    "documento": documento,
                    **info,
                    **soat,
                    **rtm,
                    "estado": "OK"
                })

            except Exception as e:

                print("Error con placa", placa, e)

                resultados.append({
                    "placa": placa,
                    "documento": documento,
                    "estado": "ERROR",
                    "error": str(e)
                })

            time.sleep(random.uniform(3,6))

    finally:

        driver.quit()

    guardar_excel(resultados)


if __name__ == "__main__":
    main()