import pyodbc
from config.settings import DB_CONFIG


def obtener_consultas_db():

    conn = pyodbc.connect(
        f"DRIVER={DB_CONFIG['DRIVER']};"
        f"SERVER={DB_CONFIG['SERVER']};"
        f"DATABASE={DB_CONFIG['DATABASE']};"
        f"UID={DB_CONFIG['UID']};"
        f"PWD={DB_CONFIG['PWD']};"
    )

    cursor = conn.cursor()

    cursor.execute("EXEC sp_consultar_runt")

    consultas = [
        {"placa": row.placa, "documento": str(row.documento)}
        for row in cursor.fetchall()
    ]

    conn.close()

    return consultas