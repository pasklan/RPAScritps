# recupera linhas do Excel para preencher um formulário na Web

from selenium import webdriver as selenium_options

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pyautogui as wait_time

from openpyxl import load_workbook

# -------------- Abrindo Arquivo Excel --------------
nomeArquivo = "C:\\RPA\\scripts\\ExcelTest\\form_web.xlsx"

instance_Excel = load_workbook(nomeArquivo)

planilha_selecionada = instance_Excel['Dados']


for linha in range(2, len(planilha_selecionada['A']) + 1):
    
    nome = planilha_selecionada[f'A{linha}'].value
    email = planilha_selecionada[f'B{linha}'].value
    telefone = planilha_selecionada[f'C{linha}'].value
    sexo = planilha_selecionada[f'D{linha}'].value
    escreva_algo = planilha_selecionada[f'E{linha}'].value
    

    # -------------- Abrindo Navegador --------------

    browser = selenium_options.Chrome()

    url = "https://pt.surveymonkey.com/r/WLXYDX2"
    browser.get(url)
    # ao se usar  a funcao WebDriverWait, a execução aguarda até 10 segundos
    # a página ser carregada
    espera = WebDriverWait(browser, 10)
    

    # -------------- Preenchendo Formulário --------------

    # captura o elemento input 'Nome completo' do DOM
    # ao se usar o expected_wait o código aguardara o elemento carregar no
    # DOM para poder ser manipulado
    name = espera.until(EC.presence_of_element_located((By.ID, "166517069")))
    # altera o valor do campo input
    name.send_keys(nome)
    
    # captura o elemento input 'Email' do DOM
    mail = espera.until(EC.presence_of_element_located((By.ID, "166517072")))
    # altera o valor do campo input
    mail.send_keys(email)

    # captura o elemento input 'Telefone' do DOM
    phone = espera.until(EC.presence_of_element_located((By.ID, "166517070")))
    # altera o valor do campo input
    phone.send_keys(telefone)

    # captura o elemento input 'Escreva algo sobre você' do DOM
    descricao = espera.until(EC.presence_of_element_located((By.ID, "166517073")))
    # altera o valor do campo input
    descricao.send_keys(escreva_algo)

    # captura o elemento radio 'Sexo' do DOM, padrão é clicar
    # no 'Masculino'
    if sexo == 'M':
        radio_button = espera.until(EC.element_to_be_clickable((By.ID, "166517071_1215509812_label")))
        wait_time.sleep(1)
        radio_button.click()
    else:
        radio_button = espera.until(EC.element_to_be_clickable((By.ID, '166517071_1215509813_label')))
        wait_time.sleep(1)
        radio_button.click()

    # Clica no botão de Enviar
    enviar = espera.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn')))
    # enviar.submit()
    wait_time.sleep(3)
