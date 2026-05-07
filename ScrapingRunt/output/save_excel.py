import pandas as pd


def save(data):

    df = pd.DataFrame(data)

    df.to_excel("runt_massivo.xlsx",index=False)