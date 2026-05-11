import pyodbc
from config.settings import DB_CONFIG


def obtener_codigo_vehiculo(placa):

    conn = pyodbc.connect(
        f"DRIVER={DB_CONFIG['DRIVER']};"
        f"SERVER={DB_CONFIG['SERVER']};"
        f"DATABASE={DB_CONFIG['DATABASE']};"
        f"UID={DB_CONFIG['UID']};"
        f"PWD={DB_CONFIG['PWD']};"
    )

    cursor = conn.cursor()

    cursor.execute("EXEC dbo.sp_consultar_Codigo_vehiculo ?", placa)

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None