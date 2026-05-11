from datetime import datetime
import os


def log_resultado(placa, documento, estado):

    carpeta = "logs"
    os.makedirs(carpeta, exist_ok=True)

    nombre = os.path.join(carpeta, f"runt_log_{datetime.now().strftime('%Y%m%d')}.txt")

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    linea = f"{fecha} | {placa} | {documento} | {estado}\n"

    with open(nombre, "a", encoding="utf-8") as f:
        f.write(linea)