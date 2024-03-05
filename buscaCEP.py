# recupera uma lista de CEPs em uma planilha Excel e salva em outro arquivo os
# endereços completos

from openpyxl import load_workbook
import os

from selenium import webdriver as driver

from selenium.webdriver.common.by import By
import pyautogui as waitTime

# ------------------------------ Carregando Planilha com a Lista de CEP ------------------------------

file_endereco_cep = 'C:\\RPA\\scripts\\ExcelTest\\endereco_cep.xlsx'

sheetAddress = load_workbook(file_endereco_cep)

selected_sheet1 = sheetAddress['Lista']
selected_sheet2 = sheetAddress['CEP']

# ------------------------------ Inicia pesquisa no navegador------------------------------

# Abre site no navegador
browser = driver.Chrome()
browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
waitTime.sleep(2)


# ------------------------------ Lendo Arquivo Excel ------------------------------


for linha in range(2, len(selected_sheet2['A']) + 1):
    waitTime.sleep(1)
    
    cep_pesquisa = selected_sheet2['A%s' % linha].value.strip()
    print(cep_pesquisa)
    # Procura e popula campo de pesquisa do CEP / pode ser tanto
    browser.find_element(By.ID, 'endereco').send_keys(cep_pesquisa) # CEP a ser pesquizado
    waitTime.sleep(2)

    # abaixo obtem o mesmo resultado mas simula um click do mouse em cima do botão
    browser.find_element(By.NAME, 'btn_pesquisar').click()
    waitTime.sleep(2)
    
    try:
        
        # captura o nome da rua
        street = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
        # captura o nome do bairro
        district = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
        # captura o nome da cidade
        cityUF = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
        # captura o nome da cidade
        CEP = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
        
    except Exception as e:
        street = 'CEP Inválido - Não foi possível encontrar a cidade'
        district = 'CEP Inválido - Não foi possível encontrar bairro'
        cityUF = 'CEP Inválido - Não foi possível encontrar UF'
        CEP = 'CEP Inválido - Não foi possível encontrar o CEP'
    
    # Seleciona a última linha preenchida na coluna A acrescentamos + 1 para 
    # iniciar na linha 2
    
    current_line = len(selected_sheet1['A']) + 1
    # converte a linha selecionada para String e concatena, ficará 'A1'
    columnA = "A" + str(current_line)
    columnB = "B" + str(current_line)
    columnC = "C" + str(current_line)
    columnD = "D" + str(current_line)

    # grava as informações do recuperadas do site na planilha
    selected_sheet1[columnA] = street
    selected_sheet1[columnB] = district
    selected_sheet1[columnC] = cityUF
    selected_sheet1[columnD] = CEP

    # clica no botao de Nova Busca
    browser.find_element(By.ID, 'btn_nbusca').click()
    

# Salva com as alterações
sheetAddress.save(filename=file_endereco_cep)

os.startfile(file_endereco_cep)
