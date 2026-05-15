from multiprocessing import Process
from funtions.dividir_lista import dividir_lista
from funtions.procesar_consultas import procesar_consultas
from db.obtener_consultas_db import obtener_consultas_db
from multiprocessing import freeze_support


def main():

    CONSULTAS = obtener_consultas_db()
    print(f"Total placas: {len(CONSULTAS)}")
    workers = 4
    bloques = dividir_lista(CONSULTAS, workers)
    procesos = []

    for i in range(workers):
        p = Process(target=procesar_consultas, args=(bloques[i], i+1))
        p.start()
        procesos.append(p)

    for p in procesos:
        p.join()

    print("Proceso completado.")


if __name__ == "__main__":
    freeze_support()
    main()