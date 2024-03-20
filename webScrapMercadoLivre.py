# Navigate to MercadoLivre.com, search for the word 'carteira' and retrieve prices

from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pyautogui as waiting_time

from openpyxl import load_workbook

import os

# open Excel file
file_path = "C:\\RPA\\scripts\\ExcelTest\\carteiras.xlsx"
excel_instance = load_workbook(file_path)
select_sheet = excel_instance["Dados"]

#open browser
browser = wb.Chrome()
browser.get("https://www.mercadolivre.com.br/")


# input the word in the serach box
browser.find_element(By.NAME, "as_word").send_keys("carteira")
waiting_time.sleep(2)

# click submit button to search
browser.find_element(By.CLASS_NAME, "nav-search-btn").click()
waiting_time.sleep(2)

wallet_data = browser.find_elements(By.CLASS_NAME, "ui-search-layout__item")


for itens in wallet_data:
    product_name = itens.find_element(By.CLASS_NAME, "ui-search-item__title").text
    product_price = itens.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
    
    
    try:
        product_cents_price = itens.find_element(By.CLASS_NAME, "andes-money-amount__cents").text
    except:
        product_cents_price = "0"
        
        
    product_url = itens.find_element(By.TAG_NAME, 'a').get_attribute("href")
    
    product_full_price = "R$ " + product_price + "," + product_cents_price
    
    print(product_name + " - " + product_full_price + " - " + product_url)
    
    # select line 2 in the column 'A'
    line = len(select_sheet['A']) + 1

    # select the columns needed
    columnA = "A" + str(line)
    columnB = "B" + str(line)
    columnC = "C" + str(line)
        
    select_sheet[columnA] = product_name
    select_sheet[columnB] = product_full_price
    select_sheet[columnC] = product_url
    
# save data to Excel
excel_instance.save(filename=file_path)

# open the file
os.startfile(file_path)
