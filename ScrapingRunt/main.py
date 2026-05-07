from multiprocessing import Pool
from workers.worker import process_vehicle
from config.database import obtener_placas
from config.settings import MAX_WORKERS
from output.save_excel import save


def main():

    placas = obtener_placas()

    with Pool(MAX_WORKERS) as p:

        results = p.map(process_vehicle, placas)

    save(results)


if __name__ == "__main__":
    main()