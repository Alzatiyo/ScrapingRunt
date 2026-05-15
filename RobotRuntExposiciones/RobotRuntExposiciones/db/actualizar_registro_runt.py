import pymssql
from config.settings import DB_CONFIG


def actualizar_registro_runt(placa):

    conn = pymssql.connect(
        server=DB_CONFIG['SERVER'],
        user=DB_CONFIG['UID'],
        password=DB_CONFIG['PWD'],
        database=DB_CONFIG['DATABASE']
    )

    cursor = conn.cursor()

    cursor.execute(
        "EXEC sp_actualizar_registro_runt @placa = %s",
        (placa,)
    )

    conn.commit()
    conn.close()

    print(f"Nota actualizada para {placa}")