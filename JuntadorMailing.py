
from JuntaMailing import juntador
from funcoes import *

quantidade = int(input("Digite a quantidade de linhas que o novo arquivo vai gravar de cada arquivo: "))

juntador(selectdiretorio(), quantidade,  savefile())

print("Processo Finalizado!!")
input("Aperte qualquer tecla para sair: ")