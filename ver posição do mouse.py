import pyautogui
import time

print("Pressione Ctrl+C para parar...")

try:
    while True:
        posicao = pyautogui.position()  # Obtém a posição atual do mouse
        print(f"Posição do mouse: {posicao}", end="\r")  # Atualiza na mesma linha
        time.sleep(0.1)  # Aguarda 100 ms antes de atualizar novamente
except KeyboardInterrupt:
    print("\nPrograma encerrado.")
            