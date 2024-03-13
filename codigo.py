import pyautogui
import time
import pandas

#pyautogui.click - clicar
#pyauto.write - escrever
#pyauto.press - pressionar uma tecla (enter, tab, space, ctrl e etc.)
#pyautogui.hotkey("ctrl", "c") - combinação de teclas

#definindo o valor da pausa entre os passos do código
pyautogui.PAUSE = 1.5

#abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#abrir link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#pausa para o carregamento da página
time.sleep(3)

#clicar nos campos de login
pyautogui.click(x=842, y=459)
pyautogui.write("qualquercoisa@gmail.com")

#número de clicks
#pyautogui.click(x=842, y=459, clicks=2)

#passar para o próximo campo
pyautogui.press("tab")
pyautogui.write("senha")

#clicar no botão de logar
pyautogui.click(x=947, y=670)
time.sleep(3)

#importando base de dados
tabela = pandas.read_csv("produtos.csv")

#pegando as linhas da tabale com o pandas
for linha in tabela.index:
    #clique no primeiro campo
    pyautogui.click(x=891, y=326)

    #código
    #codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(tabela.loc[linha,"codigo"])
    pyautogui.press("tab")

    #marca
    #marca = tabela.loc[linha,"marca"]
    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")

    #tipo
    #tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    #categoria
    #categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")

    #preço
    #preco = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    #custo
    #custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha,"obs"]
    #verificando se a coluna não está vazia
    if not pandas.isna(obs):
        pyautogui.write(obs)
        pyautogui.press("tab")

    #enviar cadastro do produto
    pyautogui.press("enter")

    #scroll para retornar ao todo da página
    #para dar um scroll até o fim da página, use um número negativo
    pyautogui.scroll(5000)
