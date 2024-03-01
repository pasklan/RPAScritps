import time 
# importações do 'webdrive' e do 'By'
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver que será o controlador do navegador
driver = webdriver.Chrome()
# acessar URL
driver.get('http://www.google.com')
# aguarda 2s
time.sleep(2)
# procura a caixa de pesquisa do Google, que possui o name 'q'
search_box = driver.find_element(By.NAME,'q')
# digita o texto que será pesquisado na caixa de pesquisa
search_box.send_keys('Dolar Hoje')
# submete a pesquisa
search_box.submit()
# aguarda 5 segundos
time.sleep(5)
# finaliza o navegador
driver.quit()