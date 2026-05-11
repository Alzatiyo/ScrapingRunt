import pymssql
from config.settings import DB_CONFIG


def obtener_codigo_vehiculo(placa):

    conn = pymssql.connect(
        server=DB_CONFIG['SERVER'],
        user=DB_CONFIG['UID'],
        password=DB_CONFIG['PWD'],
        database=DB_CONFIG['DATABASE']
    )

    cursor = conn.cursor()

    cursor.execute("EXEC dbo.sp_consultar_Codigo_vehiculo %s", (placa,))

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None