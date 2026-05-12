
def _normalizar_rtm(reg):
    mapa = {
        "numeCerti":              "Número certificado",
        "fechaExpedicion":        "Fecha expedición",
        "fechaVigencia":          "Fecha fin vigencia",
        "nombreCda":              "Nombre CDA",
        "informacionConsistente": "Información consistente",
        "vigente":                "Vigente",
    }
    return {mapa.get(k, k): v for k, v in reg.items()}