import xlsxwriter as ExcelOptions

import os

filename = 'C:\\RPA\\scripts\\ExcelTest\\testeXLSX.xlsx'

ExcelInstance = ExcelOptions.Workbook(filename)

default_sheet = ExcelInstance.add_worksheet()

default_sheet.write("A1", "Nome")
default_sheet.write("B1", "Idade")
default_sheet.write("A2", "Amanda")
default_sheet.write("B2", 21)
default_sheet.write("A3", "Arnaldo")
default_sheet.write("B3", 45)

ExcelInstance.close()

os.startfile(filename)
