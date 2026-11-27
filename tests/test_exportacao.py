
import pandas as pd
from src.services.exportacao import exportar_resultados


def test_exportar_resultados():
    resultados = [
        {
            "texto": "Congratulations! You won a prize.",
            "classe_prevista": "spam",
            "probabilidade": 0.95
        }
    ]

    arquivo = exportar_resultados(resultados)

    dados = pd.read_csv(
        pd.io.common.BytesIO(arquivo)
    )

    assert len(dados) == 1
    assert "texto" in dados.columns
    assert "classe_prevista" in dados.columns
    assert "probabilidade" in dados.columns
    assert dados.iloc[0]["classe_prevista"] == "spam"
