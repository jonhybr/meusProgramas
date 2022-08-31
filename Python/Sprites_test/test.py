import pygame
from pygame.locals import *
from time import sleep

Display_Size = [200, 200]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

sprite = pygame.transform.scale(pygame.image.load("sprite.png"), (128, 128))

while True:
    click = False
    Display.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == MOUSEBUTTONUP:
            click = True
    if click:
        x = 32
        for spr in range(0, 3):
            Display.fill((255, 255, 255))
            Display.blit(sprite.subsurface([x, 0, 32, 32]), (20, 20))
            pygame.display.update()
            sleep(0.12)
            x += 32

    Display.blit(sprite.subsurface([0, 0, 32, 32]), (20, 20))
    pygame.display.update()
    Clock.tick(60)
