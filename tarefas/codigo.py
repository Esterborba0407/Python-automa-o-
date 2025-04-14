import pyautogui
import time
pyautogui.FAILSAFE = True
#pyautogui. click => clicar em alguma tecla 
#pyautogui. press => apertar 1 tecla 
#pyautogui.write => escrever um texto 
#pyautogui.hotkey => apertar uma combinação de teclas 

pyautogui.PAUSE= 0.5

# passo 1 = entrar no sistema da empresa  https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir  o charme 
pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("enter")
# digite o site 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espere 3 segundos 
time.sleep(3)
# abrir  o charme ")
# passo 2 = fazer o login da empresa 
pyautogui.click(x=613, y=558 )
pyautogui.write("esterborba24@gmail.com")

#preencher senha 
pyautogui.press("tab")
pyautogui.write("senhaentrar")

#botao logar 
pyautogui.press("tab")
pyautogui.press("enter")
#espera de 3s
time.sleep(3)
# passo 3 = importa essa base de dados 
import pandas as pd 
tabela= pd.read_csv ("produtos.csv")
print(tabela)
# passo 4 = cadastrar 1 produto 
for linha in tabela.index: # para cada linha da minha tabela 
    pyautogui.click(x=609, y=387)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")  # enviar
    pyautogui.scroll(10000)   # rolar pra cima (ajuste se necessário)


# passo 5 = repetir para todos os produtos 
# passo 6 = instalar o pyautogui