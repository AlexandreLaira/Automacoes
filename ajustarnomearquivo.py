import os
from funcoes import selectdiretorio

ddd = 81

caminho = selectdiretorio()
arquivos = os.listdir(caminho)

for index, arquivo in enumerate(arquivos):
    os.rename(caminho + '/' + arquivo, f'{caminho}/{ddd} part {index}.csv')