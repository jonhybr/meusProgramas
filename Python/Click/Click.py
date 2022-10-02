import pygame, random
from pygame.locals import *

pygame.init()

Display = pygame.display.set_mode((300, 300))
Clock = pygame.time.Clock()
pos = []
cores = []

cubo = pygame.Surface((20, 20))

while True:

    Display.fill((100, 100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            centro = cubo.get_rect()
            centro.center = [mousePos[0], mousePos[1]]
            if len(pos) == 0:
                pos.append(centro)
                cores.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
            else:
                cores.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
                pos.append(centro)

    for c in range(0, len(pos)):
        cubo.fill(cores[c])
        Display.blit(cubo, (pos[c][0], pos[c][1]))

    pygame.display.update()
    Clock.tick(20)
