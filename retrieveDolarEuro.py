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
print(dolarValue)


# ----------------- Pesquisa valor do Euro -----------------
# Apaga o texto da caixa ded pesquisa
browser.find_element(By.NAME, 'q').clear()
browser.find_element(By.NAME, 'q').send_keys('Euro Hoje')
computerPauseTime.sleep(1)
# Envia tecla 'ENTER' no elemento 'q' para confirmar a pesquisa
browser.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
computerPauseTime.sleep(4)
euroValue = browser.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

print(euroValue)
