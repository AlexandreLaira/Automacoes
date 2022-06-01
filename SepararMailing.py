from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename
from Separador import separador


def selectfile():
    Tk().withdraw()
    filelocal = askopenfilename()
    return filelocal

def savefile():
    Tk().withdraw()
    filesave = askdirectory()
    return filesave

quantidade = int(input("Digite a quantidade de linhas que deseja separar os arquivos: "))
separador(selectfile(), quantidade, savefile())

print("Processo Finalizado!!")
input("Aperte qualquer tecla para sair: ")

