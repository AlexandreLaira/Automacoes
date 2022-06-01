from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter import filedialog as dlg
import numpy as np

def selectdiretorio():
    Tk().withdraw()
    diretoriolocal = askdirectory()
    return diretoriolocal

def savefile():
    Tk().withdraw()
    filesave = askdirectory()
    return filesave

def selectarquivo():
    Tk().withdraw()
    arquivoselecionado =dlg.askopenfilename()
    return arquivoselecionado

def criadormailing(range_inicial, range_final, ddd, localsave):
    lista_numeros = []
    for numero in range(range_inicial, range_final):
        lista_numeros.append(str(ddd) + str(numero))

    np.savetxt(localsave + f'/Range - ddd {ddd}.csv', lista_numeros, fmt='% s', delimiter=';')