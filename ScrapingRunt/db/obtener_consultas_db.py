import pymssql
from config.settings import DB_CONFIG

def obtener_consultas_db():

    conn = pymssql.connect(
        server=DB_CONFIG['SERVER'],
        user=DB_CONFIG['UID'],
        password=DB_CONFIG['PWD'],
        database=DB_CONFIG['DATABASE']
    )

    cursor = conn.cursor()

    cursor.execute("EXEC sp_consultar_runt")

    consultas = [
        {
            "placa": row[0],
            "documento": str(row[1]),
            "tipodoc": row[2]
        }
        for row in cursor.fetchall()
    ]

    conn.close()

    return consultas