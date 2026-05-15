def resultado_valido(resultado):

    if not resultado:
        return False

    info = resultado.get("info_general")

    if not info:
        return False

    # validar que tenga campos reales
    if len(info.keys()) == 0:
        return False

    # validar que tenga placa
    if not resultado.get("placa"):
        return False

    return True