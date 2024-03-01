import pyautogui as closeApp

# caminho do app que será aberto
# Ex: C:\Users\fulano\App...
appPath = "notepad"
# Permite abrir o 'Executar como'(Run) para
# abrir qualquer App windows
closeApp.hotkey('win', 'r')
closeApp.sleep(1)
closeApp.typewrite(appPath)
closeApp.press('enter')
closeApp.sleep(2)
closeApp.typewrite('Hello World', interval=0.2)
closeApp.sleep(2)
fecharApp = closeApp.getActiveWindow()
fecharApp.close()
closeApp.sleep(1)
closeApp.click(x=2379, y=567)
