import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

Display = pygame.display.set_mode((384, 384))
rect = pygame.Surface((32, 32))
rect.fill((255, 255, 255))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    Display.fill((255, 255, 255))

    for x in range(0, 12):
        for y in range(0, 12):
            Display.blit(rect, (x * 32, y * 32))

    pygame.display.update()
