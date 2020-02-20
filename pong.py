import pygame, sys
from pygame.locals import *

# CONSTANTES
# Constantes para o tamanho da tela
LARGURA_TELA = 400
ALTURA_TELA = 300
# Será utilizado para a velocidade do jogo
FPS = 200
FPSCLOCK = pygame.time.Clock()
 
pygame.init()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("PongNet")
 
terminou = False
while not terminou:
    # Atualiza o desenho na tela
    pygame.display.update()

    # Checa os eventos do mouse:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
            FPSCLOCK.tick(FPS)
 
# Finaliza a janela do jogo
pygame.display.quit()

# Finaliza o pygame
pygame.quit()
sys.exit()
