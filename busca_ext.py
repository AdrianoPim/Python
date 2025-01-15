import tkinter as tk
import os

def buscar():
    termo = entrada.get()  # Obtém o termo digitado
    termo_formatado = termo.replace(" ", "+")
    os.system(f'start chrome "https://www.google.com/search?q={termo_formatado}"')

# Criar a janela principal
janela = tk.Tk()
janela.title("Busca no Google")

# Campo de entrada
entrada = tk.Entry(janela, width=50)
entrada.pack(pady=10)

# Botão de busca
botao = tk.Button(janela, text="Buscar", command=buscar)
botao.pack(pady=5)

# Iniciar a interface gráfica
janela.mainloop()
