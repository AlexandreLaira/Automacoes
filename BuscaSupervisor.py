# -*- coding: cp1252 -*-
import unicodedata
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time


def localfile():
    Tk().withdraw()
    filelocal = askopenfilename()
    return filelocal

def savefile():
    Tk().withdraw()
    filesave = askdirectory()
    return filesave

arquivo = localfile()
patharquivo = savefile()

def buscasupervisor(user, senha, path, arquivo):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("headless")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://172.16.0.13/isize/adm/")
    time.sleep(2)
    number = driver.find_element(By.ID, "input_username").send_keys(user)
    search = driver.find_element(By.ID, "input_password").send_keys(str(senha))
    driver.find_element(By.ID, "input_submit").click()
    time.sleep(2)

    arquivo = open(arquivo, "r", encoding='utf-8')
    nomes = []
    supervisor = []
    df = []
    for linha in arquivo:
        linha2 = linha.rstrip('\n')
        df.append(linha2)


    for index, nome in enumerate(df):
        nomeinter = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
        print(index + 1)
        driver.find_element(By.XPATH, "//*[@id='menu']/li[9]/a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='cmpName']").send_keys(nomeinter.lower())
        select = Select(driver.find_element(By.ID, "cmpType"))
        select.select_by_visible_text("Promotores")
        time.sleep(2)
        try:
            driver.find_element(By.CLASS_NAME, "active").click()
            time.sleep(2)
            scrap = BeautifulSoup(driver.page_source, "html.parser")
            operator = scrap.find('span', {'class': 'cmpGreen'}, id = False)
            text = operator.get_text().strip()
            nomes.append(nome)
            supervisor.append(text)
        except:
            nomes.append(nome)
            supervisor.append("Não encontrado")
            pass
    driver.close()
    dic = {"Nomes":nomes, "Supervisor":supervisor}
    tabela = pd.DataFrame(dic)
    tabela.to_csv(f"{path}/NomesSupervisor.csv")


#patharquivo = "C:/Users/ti/Desktop/"
login = input("Digite o login Isize: ")
senha = input("Digite a senha Isize: ")

buscasupervisor(login, senha, patharquivo, arquivo)

print("Busca finalizada!")
input("Aperte qualquer tecla para sair: ")



