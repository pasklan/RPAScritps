# recupera dados de uma tabela Web e salva num arquivo Excel

import pyautogui as waitTime

from selenium import webdriver as seleniumWB
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook

import os

# prepara arquivo Excel para ser aberto
file_name_table = r"C:\RPA\scripts\ExcelTest\TabelaWeb.xlsx"
excel_instance = load_workbook(file_name_table)


# Abre o navegador e acessa o site
browserInstance = seleniumWB.Chrome()
url = "https://rpachallengeocr.azurewebsites.net/"
browserInstance.get(url)
waitTime.sleep(2)


line = 1
i = 1

while i < 4:

    # Seleciona a planilha
    selected_sheet = excel_instance["Dados"]
    
    # captura a tabela
    tableElement = browserInstance.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    # captura linhas e colunas
    rows = tableElement.find_elements(By.TAG_NAME, 'tr')
    columns = tableElement.find_elements(By.TAG_NAME, 'td')

    for current_line in rows:
        line += 1
        line = len(selected_sheet['A']) + 1
        colunaA = "A" + str(line)
        colunaB = "B" + str(line)
        colunaC = "C" + str(line)
        
        # divide each column correctly
        current_text = current_line.text          
        new_text = current_text.split(" ")
        
        selected_sheet[colunaA] = new_text[0]
        selected_sheet[colunaB] = new_text[1]
        selected_sheet[colunaC] = new_text[2]
        
        
    i += 1
    waitTime.sleep(1)
    # Vai para a próxima página
    browserInstance.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    
else:
    print('Finish.')

excel_instance.save(filename=file_name_table)
os.startfile(file_name_table)
