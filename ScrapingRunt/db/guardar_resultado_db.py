import pyodbc
import json
from config.settings import DB_CONFIG


def guardar_resultado_db(resultados):

    conn = pyodbc.connect(
        f"DRIVER={DB_CONFIG['DRIVER']};"
        f"SERVER={DB_CONFIG['SERVER']};"
        f"DATABASE={DB_CONFIG['DATABASE']};"
        f"UID={DB_CONFIG['UID']};"
        f"PWD={DB_CONFIG['PWD']};"
    )

    cursor = conn.cursor()

    json_data = json.dumps(resultados, ensure_ascii=False)

    cursor.execute("EXEC sp_guardar_runt_json @json = ?", json_data)

    conn.commit()
    conn.close()

    print("✔ Datos enviados a SQL Server")