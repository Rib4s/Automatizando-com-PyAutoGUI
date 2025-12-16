import pyautogui

# Parar o script em caso de erro (colocar essa linha no início do programa)
pyautogui.FailSafeException # movimentar o mouse para esquerda para parar

# Função para obter um texto (input)
resposta = pyautogui.prompt(text='Texto a inserir', title='Inserção de texto')
#print(resposta)

# Função para confirmar ação (input)
confirmacao = pyautogui.confirm(text='Confirma a impressão do texto?', title='Confirmação de texto', buttons=['Sim', 'Não'])
print(resposta)

# Função aviso de alerta
pyautogui.alert(text='Aviso', title='ALERTA!', button='Ok')