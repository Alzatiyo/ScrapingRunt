import pymssql
import json
from config.settings import DB_CONFIG


def guardar_resultado_db(resultados):

    conn = pymssql.connect(
        server=DB_CONFIG['SERVER'],
        user=DB_CONFIG['UID'],
        password=DB_CONFIG['PWD'],
        database=DB_CONFIG['DATABASE']
    )

    cursor = conn.cursor()

    json_data = json.dumps(resultados[0], ensure_ascii=False)

    cursor.execute("EXEC dbo.sp_guardar_runt_json %s", (json_data,))

    conn.commit()
    conn.close()

    print("Datos enviados a SQL Server")