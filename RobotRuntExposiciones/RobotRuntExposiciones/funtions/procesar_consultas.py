import time
import random
from driver.crear_driver import crear_driver
from services.consultar import consultar
from extract.extraer_info_general import extraer_info_general
from extract.extraer_soat import extraer_soat
from extract.extraer_rtm import extraer_rtm
from funtions.log_resultado import log_resultado
from db.guardar_resultado_db import guardar_resultado_db
from config.settings import URL
from funtions.resultado_valido import resultado_valido


def procesar_consultas(consultas, worker_id):

    print(f"Worker {worker_id} procesando {len(consultas)} placas")

    driver = crear_driver()

    try:
        for i, item in enumerate(consultas, start=1):

            placa = item["placa"]
            documento = item["documento"]
            tipodoc = item["tipodoc"]

            print(f"[W{worker_id}] {i}/{len(consultas)} -> {placa}")

            try:

                driver.get(URL)
                time.sleep(3)

                html = consultar(driver, placa, documento, tipodoc)

                if not html:
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
                    guardar_resultado_db([resultado])
                    log_resultado(placa, documento, "OK")
                else:
                    log_resultado(placa, documento, "SIN_RESULTADO")

                time.sleep(random.uniform(3,6))

            except Exception as e:
                print(f"[W{worker_id}] Error {placa}: {e}")
                log_resultado(placa, documento, "ERROR")
                time.sleep(3)

    finally:
        driver.quit()
