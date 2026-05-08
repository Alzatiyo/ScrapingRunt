from selenium.webdriver.common.by import By


def extraer_tabla_mat(contenedor):

    registros = []

    headers_elems = contenedor.find_elements(
        By.XPATH, ".//mat-header-row//mat-header-cell | .//thead//th")
    headers = [h.text.strip() for h in headers_elems]

    filas = contenedor.find_elements(
        By.XPATH, ".//mat-row | .//tbody//tr[td]")

    for fila in filas:
        celdas = fila.find_elements(By.XPATH, ".//mat-cell | .//td")
        if not celdas:
            continue
        registro = {}
        for i, celda in enumerate(celdas):
            key = headers[i] if i < len(headers) else f"col_{i}"
            if key:                             # omitir columnas sin encabezado
                registro[key] = celda.text.strip()
        if any(v for v in registro.values()):
            registros.append(registro)

    return registros