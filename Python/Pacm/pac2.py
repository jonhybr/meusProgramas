import pygame
from pygame.locals import *

Display_Size = (500, 400)
Display = pygame.display.set_mode(Display_Size)
fps = pygame.time.Clock()

mapa = [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

while True:
    Display.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    y = 10
    for camada in mapa:
        t = int((Display_Size[1] - 20) / len(mapa))
        print(t)
        x = (Display_Size[0] - (t * len(camada))) / 2
        for pos in camada:
            if pos == "1":
                Display.blit(pygame.Surface((t, t)), (x, y))
            x += t
        y += t
    pygame.display.update()
    fps.tick(60)
