import pygame, sys
from pygame.locals import *
 
# CONSTANTES
# Constantes para o tamanho da tela
LARGURA_TELA = 400
ALTURA_TELA = 300
# Será utilizado para a velocidade do jogo
FPS = 200
 
#Função principal
def main():
    pygame.init()
    global DISPLAY
 
    FPSCLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption('PongNet')
    terminou = False
    while not terminou: #Loop principal do jogo
        for event in pygame.event.get():
            if event.type == QUIT:
              terminou = True

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    
    # Finaliza a janela do jogo
    pygame.display.quit()
    # Finaliza o pygame
    pygame.quit()
    sys.exit()

# Se este for o único módulo, ou seja, o módulo main, execute diretamente a função main.
if __name__=='__main__':
    main()
