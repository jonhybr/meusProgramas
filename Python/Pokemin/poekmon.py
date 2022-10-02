import pygame
from pygame.locals import *
from commons import *
from random import randint


pygame.init()

Display_Size = [500, 500]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

player = pygame.Surface((32, 32))
player_col = player.get_rect()
player_move = [0, 0]


def terminate():
    pygame.quit()
    quit()


def main():
    game_loop()


def game_loop():
    movex = 0
    movey = 0
    moving = False
    grama = pygame.Surface((100, 100))
    grama.fill((100, 200, 100))
    grama_pos = grama.get_rect()
    grama_pos.x = 200
    grama_pos.y = 200
    while True:
        Display.fill((200, 200, 200))

        if player_move[0] != 0:
            player_col.x += player_move[0]
            movex += player_move[0]
            if movex == 32 or movex == -32:
                if not moving:
                    player_move[0] = 0
                movex = 0

        if player_move[1] != 0:
            player_col.y += player_move[1]
            movey += player_move[1]
            if movey == 32 or movey == -32:
                if not moving:
                    player_move[1] = 0
                movey = 0

        if moving and player_move[0] == 0 or moving and player_move[1] == 0:
            if player_col.colliderect(grama_pos):
                battle()

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:

                if event.key == K_RIGHT:
                    player_move[0] = 4
                if event.key == K_LEFT:
                    player_move[0] = -4
                if event.key == K_DOWN:
                    player_move[1] = 4
                if event.key == K_UP:
                    player_move[1] = -4
                    
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_RIGHT or event.key == K_LEFT or event.key == K_UP or event.key == K_DOWN:
                    moving = False

        Display.blit(grama, grama_pos)
        Display.blit(player, (player_col.x, player_col.y))

        pygame.display.update()
        Clock.tick(60)


def battle():
    num = randint(0, 100)
    if num != 20:
        return
    vida = pygame.Surface((100, 100))
    while True:
        Display.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
        vida.blit(vida, (100, 100))
        pygame.display.update()
        Clock.tick(60)


if __name__ == '__main__':
    main()
