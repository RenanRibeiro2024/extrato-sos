import streamlit as st

#______________________________________________________________ Configuração da página
st.set_page_config(page_title="extrato-sos", layout="wide")
st.title("📊 Extrato-SOS - Análise Financeira de Extratos")

#______________________________________________________________ Inicializa session state para armazenar os extratos
if "extratos" not in st.session_state:
    st.session_state["extratos"] = {}

#______________________________________________________________  Upload dos arquivos
uploaded_files = st.file_uploader("📎 Carregue uma ou mais faturas (CSV ou Excel)", type=["csv", "xls", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        nome_arquivo = uploaded_file.name
        print(nome_arquivo)

        with st.expander(f"📄 {nome_arquivo}", expanded=True):
            layout = st.selectbox("Layout da fatura", ["Nubank", "Banco Inter"], key=f"layout_{nome_arquivo}")

