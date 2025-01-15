import pyautogui
import time
import os

busca = input("o que deseja buscar")
s
# Passo 1: Abrir o Google Chrome na página inicial do Google
os.system('start chrome "https://www.google.com/search?q="' + busca)
time.sleep(5)  # Aguarda 5 segundos para o Chrome carregar

print("Pesquisa realizada com sucesso!")
    