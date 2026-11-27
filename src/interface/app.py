
import streamlit as st
import pandas as pd


# ==========================================
# CONFIGURAÇÕES DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="Detector de Spam",
    page_icon="📩",
    layout="centered"
)

st.title("Detector de mensagens indesejadas")
st.write("Bem-vindo ao sistema de classificação de mensagens.")


# ==========================================
# HISTÓRICO DE ANÁLISES
# ==========================================

if "historico" not in st.session_state:
    st.session_state.historico = []

st.divider()
st.subheader("Histórico de análises")

if st.session_state.historico:
    st.dataframe(st.session_state.historico)
else:
    st.info("Nenhuma análise realizada até o momento.")


# ==========================================
# ANÁLISE DE UMA MENSAGEM
# ==========================================

st.divider()
st.subheader("Analisar uma mensagem")

mensagem = st.text_area(
    "Digite a mensagem que deseja analisar:"
)

modelo_selecionado = st.selectbox(
    "Escolha o modelo:",
    [
        "Regressão Logística",
        "Árvore de Decisão"
    ]
)

if st.button("Analisar mensagem"):
    if mensagem.strip() == "":
        st.warning("Digite uma mensagem antes de continuar.")
    else:
        st.write(f"Modelo selecionado: {modelo_selecionado}")
        st.info("A classificação será implementada em breve.")


# ==========================================
# ANÁLISE DE VÁRIAS MENSAGENS
# ==========================================

st.divider()
st.subheader("Analisar várias mensagens")

arquivo = st.file_uploader(
    "Envie um arquivo CSV:",
    type=["csv"]
)

if arquivo is not None:
    try:
        dados = pd.read_csv(arquivo)

        if "texto" not in dados.columns:
            st.error("O arquivo precisa conter uma coluna chamada 'texto'.")

        elif dados.empty:
            st.warning("O arquivo não possui registros.")

        elif (
            dados["texto"].isna().any()
            or (dados["texto"].astype(str).str.strip() == "").any()
        ):
            st.warning(
                "O arquivo contém mensagens vazias. "
                "Corrija os dados antes de continuar."
            )

        else:
            st.success("Arquivo carregado com sucesso!")
            st.write("Prévia das mensagens:")
            st.dataframe(dados.head())

    except Exception as erro:
        st.error(f"Não foi possível ler o arquivo: {erro}")


# ==========================================
# EXPORTAÇÃO DE RESULTADOS
# ==========================================

st.divider()
st.subheader("Exportar resultados")

if st.button("Exportar resultados"):
    st.warning(
        "Ainda não existem resultados de classificação para exportar."
    )


# ==========================================
# DETALHES DA CLASSIFICAÇÃO
# ==========================================

st.divider()
st.subheader("Detalhes da classificação")

st.write("Quando os modelos estiverem integrados, serão exibidos aqui:")
st.write("- Classe prevista: spam ou ham")
st.write("- Probabilidade estimada")
st.write("- Modelo utilizado")
