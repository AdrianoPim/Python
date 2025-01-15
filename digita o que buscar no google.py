import pyautogui
import time
import os

# Pede ao usuário para digitar o termo de busca
busca = input("O que você quer buscar no Google? ")

# Substitui os espaços por '+' para formar a URL de busca
busca_formatada = busca.replace(" ", "+")

# Passo 1: Abrir o Google Chrome diretamente com a busca formatada
os.system(f'start chrome "https://www.google.com/search?q={busca_formatada}"')
time.sleep(5)  # Aguarda 5 segundos para o Chrome carregar

print("Pesquisa realizada com sucesso!")