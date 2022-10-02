import pygame
from pygame.locals import *

pygame.init()
Clock = pygame.time.Clock()

Display_Width = 500
Display_Height = 400

Display = pygame.display.set_mode((Display_Width, Display_Height))

personagem = pygame.Surface((32, 32))
personagem_pos = personagem.get_rect()
personagem_pos.x = 100
personagem_pos.y = 100


move = [0, 0]
moves = {'Right': False, 'Left': False, 'Up': False, 'Down': False}


while True:
    Display.fill((255, 255, 255))

    for movimento in moves.items():
        if movimento[1]:
            if movimento[0] == 'Right':
                print("a")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == K_RIGHT:
                moves['Right'] = True
            if event.key == K_LEFT:
                moves['Left'] = True
            if event.key == K_DOWN:
                moves['Down'] = True
            if event.key == K_UP:
                moves['Up'] = True

        if event.type == KEYUP:
            if event.key == K_RIGHT and moves['Right']:
                moves['Right'] = False

    Display.blit(personagem, personagem_pos)

    pygame.display.update()
    Clock.tick(60)
