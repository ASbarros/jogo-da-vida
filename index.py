import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Função para inicializar o tabuleiro com células vivas e mortas aleatoriamente
def inicializar_tabuleiro(tamanho):
    tabuleiro = np.random.choice([0, 1], tamanho*tamanho, p=[0.5, 0.5]).reshape(tamanho, tamanho)
    return tabuleiro

# Função para calcular o próximo estado do tabuleiro baseado nas regras do Jogo da Vida
def proximo_estado(tabuleiro, tamanho):
    novo_tabuleiro = np.copy(tabuleiro)
    for i in range(tamanho):
        for j in range(tamanho):
            vizinhos = tabuleiro[i-1:i+2, j-1:j+2].sum() - tabuleiro[i, j]
            if tabuleiro[i, j] == 1:
                if vizinhos < 2 or vizinhos > 3:
                    novo_tabuleiro[i, j] = 0
            else:
                if vizinhos == 3:
                    novo_tabuleiro[i, j] = 1
    return novo_tabuleiro

# Função para atualizar a animação a cada nova geração
def atualizar(frameNum, img, tabuleiro, tamanho):
    novo_estado = proximo_estado(tabuleiro, tamanho)
    img.set_data(novo_estado)
    tabuleiro[:] = novo_estado[:]
    return img,

# Definindo o tamanho do tabuleiro
tamanho = 50

# Inicializando o tabuleiro
tabuleiro = inicializar_tabuleiro(tamanho)

# Criando a figura
fig, ax = plt.subplots()
img = ax.imshow(tabuleiro, interpolation='nearest')
ani = animation.FuncAnimation(fig, atualizar, fargs=(img, tabuleiro, tamanho), frames=100, interval=50, save_count=50)
plt.show()
