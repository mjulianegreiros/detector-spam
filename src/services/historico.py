
from pathlib import Path
import pandas as pd


def salvar_analise(
    texto,
    modelo,
    threshold,
    classe_prevista,
    probabilidade
):
    caminho = (
        Path(__file__).resolve().parents[2]
        / "exports"
        / "historico.csv"
    )

    caminho.parent.mkdir(parents=True, exist_ok=True)

    nova_analise = pd.DataFrame([{
        "texto": texto,
        "modelo": modelo,
        "threshold": threshold,
        "classe_prevista": classe_prevista,
        "probabilidade": probabilidade
    }])

    if caminho.exists():
        nova_analise.to_csv(
            caminho,
            mode="a",
            header=False,
            index=False,
            encoding="utf-8-sig"
        )
    else:
        nova_analise.to_csv(
            caminho,
            index=False,
            encoding="utf-8-sig"
        )
