import pygetwindow as gw

# Lista todas as janelas abertas
windows = gw.getAllTitles()

# Exibe as janelas encontradas
print("Janelas abertas:", windows)

# Encontra a janela do navegador pelo título (parcial)
for window_title in windows:
    if 'Google Chrome' in window_title or 'Mozilla Firefox' in window_title:  # Ajuste para o navegador que você usa
        window = gw.getWindowsWithTitle(window_title)[0]
        window.minimize()  # Minimiza a janela
        print(f'Janela "{window_title}" minimizada.')
        break
else:
    print("Nenhuma janela do navegador encontrada.")
