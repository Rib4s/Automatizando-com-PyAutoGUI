import pyautogui

pyautogui.typewrite('# Ola Mundo!\n', interval=0.05) # escreve algo na tela, o intervalo define a velocidade da escrita
# pyautogui.write('Ola Mundo!', interval=0.10) (uso não convencional)

pyautogui.press('enter') # pressiona uma tecla definida na função
pyautogui.press('enter')
pyautogui.press('enter')

# Combinação de tecla pressionada
pyautogui.keyDown('shift')
pyautogui.typewrite('# ribas')
pyautogui.keyUp('shift', '\n')

# Atalhos de teclas
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('ctrl', 'shift', 'esc')
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('alt', 'tab')

# Função sleep
pyautogui.typewrite('# Boa\n')
pyautogui.sleep(2)
pyautogui.typewrite('# Noite\n')

# Função pause
pyautogui.PAUSE = 2
pyautogui.typewrite('# Bom\n')
pyautogui.typewrite('# Dia\n')
pyautogui.hotkey('ctrl', 'shift', 'esc')

# Função screenshot
pyautogui.screenshot('captura_tela.png')

# Localização através de imagem (locateOnScreen)
# O print para salvar a imagem de referência pode ser feito de maneira manual ou então através do aplicativo Flameshot ou ferramenta de captura
pyautogui.hotkey('alt', 'tab')
pyautogui.sleep(1.5)
local = pyautogui.locateOnScreen('image.png', confidence=0.9) # https://dash.plotly.com/dash
pyautogui.click(local)
pyautogui.sleep(1.5)
pyautogui.hotkey('alt', 'tab')
print(local)
pyautogui.typewrite('# Seu script foi executado com sucesso!', interval=0.07)

# Seu script foi executado com sucesso!
