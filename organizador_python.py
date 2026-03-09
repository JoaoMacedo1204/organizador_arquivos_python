#biblioteca para manipular arquivos
import os

#importa uma unica funcao da biblioteca
from tkinter.filedialog import askdirectory

#selecao e criacao de um caminho do arquivo
caminho = askdirectory(title="Selecione uma pasta")

#cria um diretorio para os arquivos
arquivos_na_pasta = os.listdir(caminho)

#dicionario para a separacao dos arquivos em lista de acordo com as suas extensoes
locais = {
    "Imagens": [".jpeg", ".png", ".bmp", ".gif", ".jpg"],
    "Planilhas": [".xlsx", ".xlsm", ".csv"],
    "PDFs": [".pdf"],
    "Texto": [".txt", ".docx"],
}

#percorre cada arquivo na lista de arquivos
for arquivo in arquivos_na_pasta:
    #une as duas partes do caminho
    caminho_arquivo = os.path.join(caminho, arquivo)
    #verifica se realmente é um arquivo
    if os.path.isfile(caminho_arquivo):
        #identifica e separa a extensao do nome do arquivo, e padroniza a formatacao da extencao
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        #analisa se a extensao esta em localizada em alguma pasta do dicionario
        for pasta in locais:
            if extensao in locais[pasta]:
                #cria o caminho da nova pasta
                nova_pasta = os.path.join(caminho, pasta)
                #verifica se o caminho existe dentro da pasta
                if not os.path.exists(nova_pasta):
                    #se nao existir, cria-se a pasta
                    os.mkdir(nova_pasta)
                #movimenta o arquivo e renomeia eles de acordo com a pasta
                os.rename(caminho_arquivo, os.path.join(nova_pasta, arquivo))       #obs:linha de codigo fora do if, para criar a pasta independente de existir ou nao