import time
import math
import win32api
import win32con

# Função para simular o clique do mouse diretamente usando pywin32
def click_mouse(x, y):
    win32api.SetCursorPos((int(x), int(y)))  # Mover o mouse para (x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # Pressionar
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)    # Soltar

# Aguarda 3 segundos para abrir manualmente o MS Paint
time.sleep(1)

# Primeiro clique na posição (318, 110)
click_mouse(318, 110)
time.sleep(1)  # Aguarda 1 segundo antes de começar a desenhar o círculo
click_mouse(1205, 104)
time.sleep(1)  # Aguarda 1 segundo antes de começar a desenhar o círculo

# Obter as dimensões da tela
largura, altura = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
centro_x, centro_y = largura // 2, altura // 2

# Definir o tamanho do círculo
raio = 100

# Desenhar o círculo clicando em cada ponto (com tempo entre cada clique)
for angulo in range(0, 361, 5):  # Gera ângulos de 0 a 360 graus
    x = centro_x + raio * math.cos(math.radians(angulo))
    y = centro_y + raio * math.sin(math.radians(angulo))
    click_mouse(x, y)  # Clica em cada ponto para simular o desenho
    time.sleep(0.05)  # Aguarda 50 ms entre cada clique

print("Círculo desenhado com sucesso!")
