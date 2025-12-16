import pyautogui

# Script para localização coordenadas do mouse
print('Aperte Ctrl + C para sair.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = ' X: ' + str(x).rjust(4) + ' / Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

# Movimento absoluto
pyautogui.moveTo(x=740, y=1055, duration=2)

# Movimento relativo
pyautogui.moveRel(xOffset=-717, yOffset=-805, duration=2)

# Movimento clique e arraste
pyautogui.mouseDown(x=159, y=149)
pyautogui.moveTo(x=1900, y=400, duration=2)
pyautogui.mouseUp()

# Movimento com clique pressionado
pyautogui.moveTo(x=159, y=149, duration=1)
pyautogui.dragTo(x=1900, y=400, duration=1)

# Tipos de cliques
pyautogui.click(x=150, y=125, clicks=1, duration=0) # clica em uma coordenada específica
pyautogui.click(x=145, y=145, clicks=1, duration=0) # clica em uma coordenada específica
pyautogui.doubleClick() # clique duplo
pyautogui.tripleClick() # clique triplo
pyautogui.rightClick(x=150, y=125) # clica em uma coordenada específica com o botão direito
pyautogui.middleClick(x=150, y=125) # clica em uma coordenada específica com o botão do meio

# Movimmento scroll
pyautogui.scroll(clicks=2000) # valores positivos rolar para cima
pyautogui.scroll(clicks=-2000) # valores negativos rolar para cima baixo
