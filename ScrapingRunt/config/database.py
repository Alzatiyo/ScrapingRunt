import pyodbc
from config.settings import SQL_CONNECTION


def obtener_placas():

    conn = pyodbc.connect(SQL_CONNECTION)

    query = """
    SELECT TOP 2
        TRIM(t926.f926_matricula) AS placa,
        TRIM(t925.f925_nit) AS documento
    FROM dbo.t926_vh_vehiculos t926
    INNER JOIN dbo.t925_vh_propietarios t925 
        ON t926.f926_rowid_propietario = t925.f925_rowid
    WHERE t926.f926_matricula = 'HYU017'
    """

    cursor = conn.cursor()
    cursor.execute(query)

    data = []

    for row in cursor.fetchall():

        data.append({
            "placa": row.placa,
            "documento": str(row.documento)
        })

    conn.close()

    return data