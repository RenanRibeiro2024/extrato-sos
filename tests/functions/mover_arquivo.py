import os

# Função que remove arquivo antigo
def verificar_e_remover_arquivo(pasta, nome_arquivo):
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    if os.path.isfile(caminho_arquivo):
        os.remove(caminho_arquivo)
