import pygame, sys
from pygame.locals import *
 
# CONSTANTES
# Constantes para o tamanho da tela
LARGURA_TELA = 400
ALTURA_TELA = 300
# Será utilizado para a velocidade do jogo
FPS = 200

# Valores para o desenho das paletas e do fundo
LARGURA_LINHA = 10
PALETA_TAMANHO = 50
PALETAOFFSET = 20

# Cores
PRETO = (0, 0, 0)
BRANCO = (255,255,255)

# Função para desenhar o fundo
def desenhaArena():
    DISPLAY.fill(PRETO)
    # Desenha a quadra
    pygame.draw.rect(DISPLAY, BRANCO, ((0,0),(LARGURA_TELA,ALTURA_TELA)), LARGURA_LINHA*2)
    # Desenha a linha no centro
    pygame.draw.line(DISPLAY, BRANCO, ((LARGURA_TELA//2),0),((LARGURA_TELA//2),ALTURA_TELA), (LARGURA_LINHA//4))

# Função para desenhar a paleta
def desenhaPaleta(paleta):
    #Impede da paleta ir  além da borda do fundo
    if paleta.bottom > ALTURA_TELA - LARGURA_LINHA:
        paleta.bottom = ALTURA_TELA - LARGURA_LINHA
    #Impede da paleta ir  além da borda do topo
    elif paleta.top < LARGURA_LINHA:
        paleta.top = LARGURA_LINHA
    #Desenha a paleta
    pygame.draw.rect(DISPLAY, BRANCO, paleta)

# Função para desenhar a bola
def desenhaBola(bola):
    pygame.draw.rect(DISPLAY, BRANCO, bola)
    
#altera a direção da bola e retorna ela
def moveBola(bola, bolaDirX, bolaDirY):
    bola.x += bolaDirX
    bola.y += bolaDirY
    return bola
    
#Função principal
def main():
    pygame.init()
    global DISPLAY
 
    FPSCLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption('PongNet')
    
    #Iniciando as variáveis nas posições iniciais
    #Estas variáveis serão alteradas ao longo da execução
    bolaX = LARGURA_TELA//2 - LARGURA_LINHA//2
    bolaY = ALTURA_TELA//2 - LARGURA_LINHA//2
    jogadorUm_posicao = (ALTURA_TELA - PALETA_TAMANHO) //2
    jogadorDois_posicao = (ALTURA_TELA - PALETA_TAMANHO) //2
    
    #altera a posição da bola
    bolaDirX = -1
    bolaDirY = -1
    
    #Criando os retangulos para a bola e paletas.
    paleta1 = pygame.Rect(PALETAOFFSET,jogadorUm_posicao,       LARGURA_LINHA,PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETAOFFSET - LARGURA_LINHA, jogadorDois_posicao, LARGURA_LINHA,PALETA_TAMANHO)
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)

    #Desenhando as posições iniciais da arena
    desenhaArena()
    desenhaPaleta(paleta1)
    desenhaPaleta(paleta2)
    desenhaBola(bola)

    while True: #Loop principal
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()

      desenhaArena()
      desenhaPaleta(paleta1)
      desenhaPaleta(paleta2)
      desenhaBola(bola)
      
      bola = moveBola(bola, bolaDirX, bolaDirY)

      pygame.display.update()
      FPSCLOCK.tick(FPS)

# Se este for o único módulo, ou seja, o módulo main, execute diretamente a função main.
if __name__=='__main__':
    main()
