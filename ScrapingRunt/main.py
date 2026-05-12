import time
import random
from driver.crear_driver import crear_driver
from db.obtener_consultas_db import obtener_consultas_db
from services.consultar import consultar
from extract.extraer_info_general import extraer_info_general
from extract.extraer_soat import extraer_soat
from extract.extraer_rtm import extraer_rtm
from funtions.log_resultado import log_resultado
from db.guardar_resultado_db import guardar_resultado_db
from config.settings import URL
from funtions.resultado_valido import resultado_valido


def main():

    CONSULTAS = obtener_consultas_db()
    print(f"Placas a consultar: {len(CONSULTAS)}")
    driver = crear_driver()
    todos_resultados = []

    try:

        for i, item in enumerate(CONSULTAS, start=1):

            placa = item["placa"]
            documento = item["documento"]
            tipodoc = item["tipodoc"]

            print(f"\n{'─'*50}")
            print(f"[{i}/{len(CONSULTAS)}] Consultando placa: {placa} | doc: {documento} | tipo doc: {tipodoc}")

            try:

                driver.get(URL)
                time.sleep(3)

                html = consultar(driver, placa, documento, tipodoc)

                if not html:
                    print("Consulta inválida, saltando placa...")
                    log_resultado(placa, documento, "SIN_RESULTADO")
                    continue

                info_gen = extraer_info_general(driver)
                soat = extraer_soat(driver)
                rtm = extraer_rtm(driver)

                resultado = {
                    "placa": placa,
                    "documento": documento,
                    "info_general": info_gen,
                    "soat": soat,
                    "rtm": rtm,
                }

                if resultado_valido(resultado):
                    todos_resultados.append(resultado)
                    guardar_resultado_db([resultado])
                    log_resultado(placa, documento, "OK")

                else:
                    print("Resultado inválido, no se guarda en DB")
                    log_resultado(placa, documento, "SIN_RESULTADO")


                delay = random.uniform(3,6)
                print(f"Esperando {round(delay,2)} segundos...")
                time.sleep(delay)

            except Exception as e:
                print(f"Error con placa {placa}: {e}")
                log_resultado(placa, documento, "ERROR")
                time.sleep(3)

    finally:
        driver.quit()

    print("Proceso completado.")

    return todos_resultados


if __name__ == "__main__":
    main()