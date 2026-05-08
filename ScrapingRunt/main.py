from driver.crear_driver import crear_driver
from db.obtener_consultas_db import obtener_consultas_db
from services.consultar import consultar
from extract.extraer_info_general import extraer_info_general
from extract.extraer_soat import extraer_soat
from extract.extraer_rtm import extraer_rtm
from storage.guardar_json import guardar_json
from db.guardar_resultado_db import guardar_resultado_db
from request.enviar_api import enviar_api


def main():

    CONSULTAS = obtener_consultas_db()

    print(f"Placas a consultar: {len(CONSULTAS)}")

    driver = crear_driver()
    todos_resultados = []

    try:
        for item in CONSULTAS:

            placa = item["placa"]
            documento = item["documento"]

            print(f"\nConsultando placa: {placa}")

            html = consultar(driver, placa, documento)

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

            todos_resultados.append(resultado)

            print(
                f"Resultado → "
                f"SOAT: {'SI' if soat else 'NO'} | "
                f"RTM: {'SI' if rtm else 'NO'}"
            )

    finally:
        guardar_json(todos_resultados)
        guardar_resultado_db(todos_resultados)
        enviar_api(todos_resultados, idInterface=1530)

        input("\nEnter para cerrar navegador...")
        driver.quit()

    print("\nProceso completado.")
    return todos_resultados

if __name__ == "__main__":
    main()