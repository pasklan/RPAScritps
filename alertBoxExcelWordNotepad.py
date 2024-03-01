# Simple message box that waits for the user to choose which app to open: Excel / Word / Notepad

import pyautogui
import pyautogui as choice

option = pyautogui.confirm('Escolha uma Opção:', buttons = ['Excel', 'Word', 'Bloco de Notas'])


# 'Abre o Excel'
if option == 'Excel':
    choice.hotkey('win', 'r')
    choice.sleep(2)
    choice.typewrite('Excel')
    choice.press('enter')
    
    
# 'Abre o Word'
elif option == 'Word':
    choice.hotkey('win', 'r')
    choice.sleep(2)
    choice.typewrite('winword')
    choice.press('enter')
    
    
# 'Abre o Bloco de Notas'
elif option == 'Bloco de Notas':
    choice.hotkey('win', 'r')
    choice.sleep(2)
    choice.typewrite('Notepad')
    choice.press('enter')
    choice.sleep(2)
    choice.typewrite('Bloco de notas foi escolhido.')
