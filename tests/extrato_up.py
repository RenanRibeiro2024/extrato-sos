import streamlit as st
import time
import os
import win32com.client
import pythoncom

st.set_page_config(page_title="extrato-sos", layout="wide")
st.title("📊 Extrato-SOS - Resultado Financeiro")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_ARQUIVOS = os.path.join(BASE_DIR, "..", "src", "extrato_sos", "arquivos")
PASTA_CONSOLIDADO = os.path.join(BASE_DIR, "..", "src", "extrato_sos", "consolidado")

# Garante que a pasta existe
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

        # Salva o novo
        with open(caminho_final, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"Arquivo salvo! {nome_arquivo}")

    print("================================")
    print("Arquivos carregados com sucesso!")
    print("================================")

    time.sleep(5)
    print()
    print("Atualizando consolidado...")
    print()

    # Nome fixo do consolidado
    nome_arquivo_consolidado = "consolidado.xlsx"
    caminho_final_consolidado = os.path.join(PASTA_CONSOLIDADO, nome_arquivo_consolidado)

    # =====================================================
    # 🔧 Inicializa ambiente COM para Excel
    pythoncom.CoInitialize()

    try:
        # Inicia o excel
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = 0  # roda em background

        # Abre o consolidado
        workbook = excel.Workbooks.Open(caminho_final_consolidado)

        # Atualiza dados
        workbook.RefreshAll()

        excel.CalculateUntilAsyncQueriesDone()
        #Save
        workbook.Save()


    finally:
        # Fecha Excel e descarta recursos COM
        excel.Quit()
        pythoncom.CoUninitialize()

    print("================================")
    print("Consolidado atualizado!")
    print("================================")

st.stop()
