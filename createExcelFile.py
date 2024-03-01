# import da lib de manipulação do Excel
import xlsxwriter
# import os

# import do selenium para trabalhar com o navegador
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import da lib para trabalhar com o tempo e teclas do teclado
import pyautogui as computerPauseTime

# precisa do By para usar versão mais recente
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.google.com')

# ----------------- Pesquisa valor do Dolar -----------------
computerPauseTime.sleep(1)
# Buscar elemento que é a input do tipo texto para pesquisar e enviar 'Dolar hoje'
browser.find_element(By.NAME, 'q').send_keys('Dolar Hoje')
computerPauseTime.sleep(1)
# Envia tecla 'ENTER' no elemento 'q' para confirmar a pesquisa
browser.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
computerPauseTime.sleep(1)

dolarValue = browser.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text


# ----------------- Pesquisa valor do Euro -----------------
# Apaga o texto da caixa ded pesquisa
browser.find_element(By.NAME, 'q').clear()
browser.find_element(By.NAME, 'q').send_keys('Euro Hoje')
computerPauseTime.sleep(1)
# Envia tecla 'ENTER' no elemento 'q' para confirmar a pesquisa
browser.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
computerPauseTime.sleep(4)
euroValue = browser.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text


# ----------------- Cria nova planilha -----------------

path_file_name = 'C:\\RPA\\scripts\\ExcelTest\\Dolar_Euro.xlsx'
# cria a planilha no caminho especificado
workbook = xlsxwriter.Workbook(path_file_name)

# adiciona uma nova planilha na pasta de trabalho
worksheet = workbook.add_worksheet()
# escreva valores nas células
worksheet.write('A1', 'Dolar')
worksheet.write('B1', 'Euro')
worksheet.write('A2', dolarValue)
worksheet.write('B2', euroValue)
# fecha e salva a pasta de trabalho
workbook.close()