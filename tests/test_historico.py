from pathlib import Path
import pandas as pd
import src.services.historico as historico


def test_salvar_analise(monkeypatch, tmp_path):
    arquivo_fake = tmp_path / "src" / "services" / "historico.py"
    arquivo_fake.parent.mkdir(parents=True)
    arquivo_fake.touch()

    monkeypatch.setattr(
        historico,
        "__file__",
        str(arquivo_fake)
    )

    historico.salvar_analise(
        texto="Congratulations! You won a prize.",
        modelo="Regressão Logística",
        threshold=0.5,
        classe_prevista="spam",
        probabilidade=0.95
    )

    caminho_teste = tmp_path / "exports" / "historico.csv"
    dados = pd.read_csv(caminho_teste)

    assert len(dados) == 1
    assert dados.iloc[0]["texto"] == "Congratulations! You won a prize."
    assert dados.iloc[0]["classe_prevista"] == "spam"
    assert dados.iloc[0]["probabilidade"] == 0.95