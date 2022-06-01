import csv
import numpy as np

def separador(arquivo, quantidade, destino):
    lista = []
    contador = 0
    vezes = 0

    df = open(arquivo)
    tabela = csv.reader(df)

    for linha in tabela:
        if contador < quantidade:
            lista.append(linha)
            contador += 1
        else:
            lista.append(linha)
            np.savetxt(f"{destino}/ - {vezes}.csv", lista, fmt='% s')
            vezes += 1
            lista = []
            contador = 0

    np.savetxt(f"{destino}/ - {vezes}.csv", lista, fmt='% s')
