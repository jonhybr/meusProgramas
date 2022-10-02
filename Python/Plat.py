import pygame
from pygame.locals import *

pygame.init()

DWidth = 801
DHeight = 481
Display = pygame.display.set_mode((DWidth, DHeight))
Clock = pygame.time.Clock()

px = 50
py = 400
movimento = 3
movex = 0
movey = 0
personagem = pygame.Surface((15, 15))
personagem.fill((100, 100, 100))
tamanho = (32, 32)
ceu = pygame.Surface(tamanho)
ceu.fill((150, 150, 250))
terra = pygame.Surface(tamanho)
terra.fill((150, 120, 90))
grama = pygame.Surface(tamanho)
grama.fill((50, 180, 50))

gameMap = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(len(gameMap), len(gameMap[0]))

while True:

    px += movex
    py += movey

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                movex = movimento
            if event.key == K_LEFT:
                movex = -movimento
            if event.key == K_DOWN:
                movey = movimento
            if event.key == K_UP:
                movey = -movimento

        if event.type == pygame.KEYUP:
            if event.key == K_RIGHT and movex == movimento \
                    or event.key == K_LEFT and movex == -movimento:
                movex = 0
            if event.key == K_DOWN and movey == movimento \
                    or event.key == K_UP and movey == -movimento:
                movey = 0

    Display.fill((0, 0, 0))

    y = 0
    for camada in gameMap:
        x = 0
        for pos in camada:
            if pos == 0:
                Display.blit(terra, (x, y))
            if pos == 1:
                Display.blit(ceu, (x, y))
            if pos == 2:
                Display.blit(grama, (x, y))
            if pos == 3:
                Display.blit(pygame.Surface(tamanho), (x, y))
            x += tamanho[0]
        y += tamanho[1]

    Display.blit(personagem, (px, py))
    pygame.display.update()
    Clock.tick(60)
