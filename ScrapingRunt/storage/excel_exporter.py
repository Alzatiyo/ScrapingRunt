import pandas as pd


def guardar_excel(data):

    df = pd.DataFrame(data)

    df.to_excel(
        "resultado_runt.xlsx",
        index=False
    )

    print("Excel generado: resultado_runt.xlsx")