import requests
from config.settings import URL2, HEADERS
from db.obtener_codigo_vehiculo import obtener_codigo_vehiculo


def criterio_api(todos_resultados, idInterface):

    params = {
        "idCompania": 8294,
        "idInterface": idInterface,
        "idDocumento": 193612,
        "nombreDocumento": "Vehiculos Criterios"
    }

    criterios = []

    for r in todos_resultados:

        placa = r["placa"]
        info = r["info_general"]

        codigo_vehiculo = obtener_codigo_vehiculo(placa)

        criterios.append({
            "Código del vehiculo": str(codigo_vehiculo),
            "Compañia": "3",
            "ID_TIPO_VH": "1",
            "Mayor de criterio de clasificación": info.get("MARCA", ""),
            "Plan de criterio de clasificación": "001"
        })

        criterios.append({
            "Código del vehiculo": str(codigo_vehiculo),
            "Compañia": "3",
            "ID_TIPO_VH": "1",
            "Mayor de criterio de clasificación": info.get("LÍNEA", ""),
            "Plan de criterio de clasificación": "002"
        })

        criterios.append({
            "Código del vehiculo": str(codigo_vehiculo),
            "Compañia": "3",
            "ID_TIPO_VH": "1",
            "Mayor de criterio de clasificación": info.get("CILINDRAJE", ""),
            "Plan de criterio de clasificación": "003"
        })

        criterios.append({
            "Código del vehiculo": str(codigo_vehiculo),
            "Compañia": "3",
            "ID_TIPO_VH": "1",
            "Mayor de criterio de clasificación": info.get("TIPO DE SERVICIO", ""),
            "Plan de criterio de clasificación": "004"
        })

        criterios.append({
            "Código del vehiculo": str(codigo_vehiculo),
            "Compañia": "3",
            "ID_TIPO_VH": "1",
            "Mayor de criterio de clasificación": info.get("CLASE DE VEHÍCULO", ""),
            "Plan de criterio de clasificación": "005"
        })

        criterios.append({
            "Código del vehiculo": str(codigo_vehiculo),
            "Compañia": "3",
            "ID_TIPO_VH": "1",
            "Mayor de criterio de clasificación": info.get("TIPO COMBUSTIBLE", ""),
            "Plan de criterio de clasificación": "006"
        })

    body = {
        "Inicial": [{"Compañía": "3"}],
        "Criterios clientes": criterios,
        "Final": [{"Compañía": "3"}]
    }

    response = requests.post(
        URL2,
        headers=HEADERS,
        params=params,
        json=body
    )

    ##print("Status:", response.status_code)
    ##print("Respuesta:", response.text)

    return response