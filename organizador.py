import os
import shutil

pasta_origem = "C:/home/anny/Documentos"

tipos_arquivos = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Documentos": [".pdf", ".txt"],
    "Planilhas": [".xlsx", ".csv"]
}

for pasta in tipos_arquivos:
    caminho = os.path.join(pasta_origem, pasta)
    if not os.path.exists(caminho):
        os.makedirs(caminho)

for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)

    if os.path.isfile(caminho_arquivo):
        for pasta, extensoes in tipos_arquivos.items():
            if any(arquivo.lower().endswith(ext) for ext in extensoes):
                destino = os.path.join(pasta_origem, pasta, arquivo)
                shutil.move(caminho_arquivo, destino)
                print(f"Movido: {arquivo} → {pasta}")
                break

