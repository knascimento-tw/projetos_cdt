'''
Primicia - Jogo de Cartas Viradas com Pygame
'''

import pygame
import random
import time 
import os

def resolver_caminho_recurso(caminho_relativo):

    try:
        base_path = sys._MEIPASS
    except AttributeError:
        
        base_path = os.path.abspath(".")

    return os.path.join(base_path, caminho_relativo)


pygame.init()


LARGURA, ALTURA = 800, 600
COR_FUNDO = (30, 30, 30)
COR_TEXTO = (255, 255, 255)

JANELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Memória Pygame")
RELOGIO = pygame.time.Clock()


caminho_imagens = "imagens"
NOMES_IMAGENS = [
    "img01.png", "img02.png", "img03.png",
    "img04.png", "img05.png", "img06.png",
]
VERSO_NOME = "verso.png"

TAMANHO_CARTA = (100, 100)
ALTURA_PLACAR = 50
AREA_JOGO_Y = ALTURA_PLACAR

caminho_verso = resolver_caminho_recurso(os.path.join(caminho_imagens, VERSO_NOME))
try: 
    VERSO_CARTA_IMG = pygame.image.load(caminho_verso)
    VERSO_CARTA_IMG = pygame.transform.scale(VERSO_CARTA_IMG, TAMANHO_CARTA)
except pygame.error as e:
    print(f"ERRO: Não foi possível carregar o verso da carta: {e}")
    exit()

dados_imagens = []
for nome_arquivo in NOMES_IMAGENS:
    img_path = resolver_caminho_recurso(os.path.join(caminho_imagens, nome_arquivo))
    try:
        imagem_surface = pygame.image.load(img_path)
        imagem_surface = pygame.transform.scale(imagem_surface, TAMANHO_CARTA)
        dados_imagens.append((imagem_surface, nome_arquivo))
    except pygame.error as e:
        print(f"AVISO: imagem {}")