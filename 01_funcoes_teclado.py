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
