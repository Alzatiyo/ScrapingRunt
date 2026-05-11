import requests
from config.settings import URL2, HEADERS
from db.obtener_codigo_vehiculo import obtener_codigo_vehiculo


def convertir_fecha(fecha):
    if not fecha:
        return ""
    try:
        dia, mes, anio = fecha.split("/")
        return f"{anio}{mes}{dia}"
    except:
        return ""


def entidad_api(todos_resultados, idInterface):

    params = {
        "idCompania": 8294,
        "idInterface": idInterface,
        "idDocumento": 242909,
        "nombreDocumento": "entidad_dinamica_vehiculos_v3"
    }

    vehiculos = []

    for r in todos_resultados:

        placa = r.get("placa")
        codigo_vehiculo = obtener_codigo_vehiculo(placa)

        soat = r.get("soat") or {}
        rtm = r.get("rtm") or {}

        # ---------- SOAT ----------
        entidad_soat = soat.get("Entidad expide SOAT")
        fecha_soat = convertir_fecha(soat.get("Fecha fin de vigencia"))

        if entidad_soat:
            vehiculos.append({
                "F_CIA": "3",
                "f753_dato_fecha_hora": "",
                "f753_dato_texto": entidad_soat,
                "f753_id_atributo": "ENTIDAD SOAT",
                "f753_id_entidad": "GE010",
                "f753_id_grupo_entidad": "DATOS VEHICULO",
                "F926_ID": str(codigo_vehiculo)
            })

        if fecha_soat:
            vehiculos.append({
                "F_CIA": "3",
                "f753_dato_fecha_hora": fecha_soat,
                "f753_dato_texto": "",
                "f753_id_atributo": "FECHA VENCIMIENTO SOAT",
                "f753_id_entidad": "GE010",
                "f753_id_grupo_entidad": "DATOS VEHICULO",
                "F926_ID": str(codigo_vehiculo)
            })

        # ---------- RTM ----------
        entidad_rtm = rtm.get("CDA expide RTM")
        fecha_rtm = convertir_fecha(rtm.get("Fecha Vigencia"))

        if entidad_rtm:
            vehiculos.append({
                "F_CIA": "3",
                "f753_dato_fecha_hora": "",
                "f753_dato_texto": entidad_rtm,
                "f753_id_atributo": "ENTIDAD RTM",
                "f753_id_entidad": "GE011",
                "f753_id_grupo_entidad": "DATOS VEHICULO",
                "F926_ID": str(codigo_vehiculo)
            })

        if fecha_rtm:
            vehiculos.append({
                "F_CIA": "3",
                "f753_dato_fecha_hora": fecha_rtm,
                "f753_dato_texto": "",
                "f753_id_atributo": "FECHA VENCIMIENTO RTM",
                "f753_id_entidad": "GE011",
                "f753_id_grupo_entidad": "DATOS VEHICULO",
                "F926_ID": str(codigo_vehiculo)
            })

    body = {
        "Inicial": [{"F_CIA": "3"}],
        "Vehiculo V": vehiculos,
        "Final": [{"F_CIA": "3"}]
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