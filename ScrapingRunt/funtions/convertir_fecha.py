def convertir_fecha(fecha):
    if not fecha:
        return ""

    try:
        dia, mes, anio = fecha.split("/")
        return f"{anio}{mes}{dia}"
    except:
        return ""