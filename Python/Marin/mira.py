import pygame
from pygame.locals import *


pygame.init()
Display_Size = (500, 400)
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

pers = pygame.Surface((16, 16))
pers_pos = pers.get_rect()
pers_pos.x = Display_Size[0] // 2 - 16
pers_pos.y = Display_Size[1] // 2 - 16

linhas = []

while True:

    Display.fill((200, 200, 200))
    mouse = pygame.mouse.get_pos()
    Display.blit(pers, pers_pos)
    pygame.draw.line(Display, (0, 0, 0), pers_pos.center, (mouse[0], mouse[1]), 3)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == MOUSEBUTTONUP:
            if event.button == BUTTON_LEFT:
                linhas.append((pers_pos.center, mouse))
            if event.button == BUTTON_RIGHT:
                pers_pos.center = (mouse[0], mouse[1])
            if event.button == BUTTON_MIDDLE:
                linhas.clear()

    if len(linhas) > 0:
        for linha in linhas:
            pygame.draw.line(Display, (0, 0, 0), linha[0], linha[1], 3)



    pygame.display.update()
