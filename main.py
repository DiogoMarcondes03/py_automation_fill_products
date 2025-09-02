import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

time.sleep (3.5)

pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("algumacoisa@hotmail.com")
pyautogui.press("tab")
pyautogui.write("senhawhateverparaacessarosite")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep (3.5)

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=1018, y=287)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)

