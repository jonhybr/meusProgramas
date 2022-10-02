import pygame
from pygame.locals import *
from random import randint

pygame.init()

Display_Size = [500, 250]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

sprites = {'personagem': pygame.transform.scale(pygame.image.load('personagem_sprite.png'), (256, 64)),
           'nuvem1': pygame.transform.scale2x(pygame.image.load('nuvem1.png')),
           'nuvem2': pygame.transform.scale2x(pygame.image.load('nuvem2.png')),
           'pedra': pygame.transform.scale2x(pygame.image.load('pedra.png'))}

running = True

personagem = [sprites['personagem'].subsurface([0, 0, 64, 64]), 0, sprites['personagem']]


def sprite_change(sprite, spriteatl, size, qtdsprites):
    spriteatl += 1
    if spriteatl == qtdsprites:
        spriteatl = 0
    return [sprite.subsurface([spriteatl * size, 0, 64, 64]), spriteatl, sprite]


run_time = 0
world_time = 10
world_sprites = [[sprites['nuvem1'], [50, 50]], [sprites['nuvem1'], [250, 70]], [sprites['nuvem2'], [320, 40]]]

while True:
    Display.fill((240, 245, 250))

    if running:
        if run_time >= 10:
            personagem = sprite_change(personagem[2], personagem[1], 64, 4)
            run_time = 0

    pygame.draw.rect(Display, (170, 220, 120), (0, 200, Display_Size[0], Display_Size[1]))
    pygame.draw.line(Display, (0, 0, 0), (0, 200), (Display_Size[0], 200), 1)

    Display.blit(personagem[0], (20, 150))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    run_time += 1
    Clock.tick(60)
    pygame.display.update()
