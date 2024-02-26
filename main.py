# biblioteca para controle de UI
import pyautogui as mousePosition

# aguarda 2 segundos antes de iniciar
mousePosition.sleep(2)
#print(mousePosition.position())

# move o ponteiro do mouse para uma posição: no caso, menu
# Start
mousePosition.moveTo(x=2760, y=1061)

# clica na coordenada especificada
mousePosition.click(x=2760, y=1061)
# aguarda 1 segundos antes de iniciar
mousePosition.sleep(1)
# digita o texto passado por parâmetro no local onde está o foco
mousePosition.typewrite('calc')

# aguarda 1 segundos antes de iniciar
mousePosition.sleep(1)
# simula o aperto de uma tecla do teclado
mousePosition.hotkey('enter')
