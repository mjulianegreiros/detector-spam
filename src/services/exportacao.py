import pandas as pd


def exportar_resultados(resultados):
    dados = pd.DataFrame(resultados)

    return dados.to_csv(index=False).encode("utf-8-sig")