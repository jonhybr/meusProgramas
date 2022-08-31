import pygame
from pygame.locals import *

pygame.init()
Display_Size = (500, 400)
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

sprites = {'coracao': pygame.transform.scale2x(pygame.image.load('coracao.png')),
           'grama': pygame.transform.scale2x(pygame.image.load('grama.png')),
           'grama_topo': pygame.transform.scale2x(pygame.image.load('grama2.png')),
           'terra': pygame.transform.scale2x(pygame.image.load('terra.png')),
           'personagem': pygame.transform.scale(pygame.image.load('personagem.png'), (72, 96))}

correndo = [pygame.transform.scale(pygame.image.load('correr1.png'), (72, 96)),
            pygame.transform.scale(pygame.image.load('correr2.png'), (72, 96)),
            pygame.transform.scale(pygame.image.load('correr3.png'), (72, 96)),
            pygame.transform.scale(pygame.image.load('correr4.png'), (72, 96)),
            pygame.transform.scale(pygame.image.load('correr5.png'), (72, 96)),
            pygame.transform.scale(pygame.image.load('correr6.png'), (72, 96))]

qvidas = 3

gsize = sprites['grama'].get_rect()

perso = sprites['personagem'].get_rect()

print(perso)

cor = 0
delay = 0
change = 1
while True:
    Display.fill((180, 220, 255))
    pygame.draw.rect(Display, (50, 50, 50), (5, 5, 123, 40), 0)
    pygame.draw.rect(Display, (20, 20, 20), (5, 5, 123, 40), 4)

    vx = 10
    for vidas in range(0, qvidas):
        Display.blit(sprites['coracao'], (vx, 10))
        vx += 40

    Display.blit(correndo[cor], (100, 100))
    Display.blit(sprites['personagem'], (150, 100))

    if delay == 160:
        if 0 <= cor <= len(correndo):
            cor += 1
        if cor >= len(correndo):
            cor = 0
        delay = 0
    delay += 1

    for pos in range(0, Display_Size[0] // gsize[2] + 1):
        Display.blit(sprites['grama_topo'], (pos * gsize[2], Display_Size[1] - gsize[3] * 3))
        Display.blit(sprites['grama'], (pos * gsize[2], Display_Size[1] - gsize[3] * 2))
        Display.blit(sprites['terra'], (pos * gsize[2], Display_Size[1] - gsize[3]))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == MOUSEBUTTONUP:
            if event.button == BUTTON_LEFT:
                qvidas -= 1
            if event.button == BUTTON_RIGHT:
                qvidas += 1

    pygame.display.update()
