import pygame
from pygame.locals import *

pygame.init()
Display_Size = (500, 400)
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

por = 100

while True:
    Display.fill((240, 240, 240))

    por = 100

    espaco = 10
    for linha in range(0, (Display_Size[1] // por)):
        pygame.draw.line(Display, (0, 0, 0), (0, Display_Size[1] - (Display_Size[1] / por)), (Display_Size[0], Display_Size[1] - (Display_Size[1] / por)))
        por -= 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
