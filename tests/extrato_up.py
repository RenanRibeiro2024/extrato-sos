import streamlit as st
import time
import os

# Função que remove arquivo antigo
def verificar_e_remover_arquivo(pasta, nome_arquivo):
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    if os.path.isfile(caminho_arquivo):
        os.remove(caminho_arquivo)

st.set_page_config(page_title="extrato-sos", layout="wide")
st.title("📊 Extrato-SOS - Análise Financeira de Extratos")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_ARQUIVOS = os.path.join(BASE_DIR, "..", "src", "extrato_sos", "arquivos")

os.makedirs(PASTA_ARQUIVOS, exist_ok=True)


uploaded_files = st.file_uploader(
    "📎 Carregue um ou mais extratos (CSV ou Excel)",
    type=["csv", "xls", "xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        nome_arquivo = uploaded_file.name
        caminho_final = os.path.join(PASTA_ARQUIVOS, nome_arquivo)

        # Remove antigo
        if os.path.isfile(caminho_final):
            os.remove(caminho_final)

        # Salva
        with open(caminho_final, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"Arquivo salvo! {nome_arquivo}")
time.sleep(15)
st.success("Arquivos processados com sucesso. Encerrando...")
st.stop()
