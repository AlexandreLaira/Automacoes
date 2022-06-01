
import os
import numpy as np
import pandas as pd


def juntador(path, quantidade, destino):
    contador = 0
    lista = []
    controle = 0
    arquivos = os.listdir(path)

    for arquivo in arquivos:

        df = pd.read_csv(path + '/' + arquivo, encoding='ANSI', sep=';')
        df = pd.DataFrame(df)

        for linha in range(len(df)):
            if controle + 1 == quantidade:
                lista.append(df.iloc[linha, ])
                controle = 0
                contador = 0
                break
            else:
                lista.append(df.iloc[linha, ])
                controle += 1
                contador += 1

    np.savetxt(f"{destino}/ArquivoJuntado.csv", lista, fmt='% s', delimiter=';')


