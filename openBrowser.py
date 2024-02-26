import pyautogui as openBrowser

openBrowser.sleep(2)
# start bar position
openBrowser.click(x=2779, y=1051)
# print(openBrowser.position())


openBrowser.sleep(1)
# search Edge App
openBrowser.typewrite('edge')
openBrowser.sleep(1)
# press Enter key
openBrowser.press('enter')
openBrowser.sleep(1)
# type the URL address
openBrowser.typewrite('https://www.google.com')

# press Enter key
openBrowser.press('enter')
openBrowser.sleep(2)
