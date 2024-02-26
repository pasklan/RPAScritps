import pyautogui as openApp

# caminho do app que será aberto, pode ser só o nome do processo, desde que o mesmo esteja no PATH do Sistema Operacional
appPath = "notepad"
# Permite abrir o 'Executar como'(Run) para abrir qualquer App windows
openApp.hotkey('win', 'r')
openApp.sleep(1)
openApp.typewrite(appPath)
openApp.press('enter')
openApp.sleep(1)
openApp.typewrite('Hello World')
