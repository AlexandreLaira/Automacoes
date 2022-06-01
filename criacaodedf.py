import numpy as np
import pandas as pd
from funcoes import selectarquivo, selectdiretorio
import unicodedata
import csv

'''
OI = 'OI Movel S.A'
VIVO = Vivo
CLARO = Claro
'''
oper = 'OI Movel S.A'
lote_nome = 'Mailing TIM - Out - Lote105 Marco'
codigoinicial = 50000280856237

caminho = selectdiretorio()
arquivo = 'ArquivoJuntado'
selecionar_arquivo = selectarquivo()

dados = open(selecionar_arquivo)
dados = csv.reader(dados, delimiter=';')
numero = []

for linha in dados:
       linha[1] = unicodedata.normalize('NFKD', linha[1]).encode('ASCII', 'ignore').decode('ASCII')
       if linha[1] == oper:
              numero.append(str(linha[0]))
       else:
              pass

codigo = []
ddd = []
telefone = []
nome = []
operadora = []
lote = []
f = []
g = []
h = []
i = []
for numeros in numero:
       ddd.append(numeros[0:2])
       telefone.append(numeros[2:11])
       codigoinicial += 1
       codigo.append(codigoinicial)
       nome.append('SEM NOME @'+ oper)
       operadora.append(oper)
       lote.append(lote_nome)
       f.append('')
       g.append('')
       h.append('')
       i.append('')

dic = {
       'Codigo':codigo, 'Nome':nome, 'DDD':ddd, 'Telefone':telefone, 'Operadora':operadora, 'f':f, 'g':g, 'h':h, 'i':i, 'Lote':lote
}

arquivoFinal = pd.DataFrame(dic)
np.savetxt(f'{caminho}/ArquivoFinal.csv', arquivoFinal, fmt='% s', delimiter=';')