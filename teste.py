
from selenium  import webdriver
import pyautogui

#variaveis
usuario = input('Digite seu usario: ')
senha = input('Digite sua senha: ')


navegador = webdriver.Chrome('chromedriver.exe')

navegador.get("https://suporte.sp.senac.br/maximo/ui/maximo.jsp")

pyautogui.PAUSE = 5
pyautogui.write(usuario)

pyautogui.PAUSE = 1
pyautogui.hotkey('tab')
pyautogui.write(senha)
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')





