import pygame
from pygame.locals import *

pygame.init()

Display_Size = [500, 500]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

player_Size = [50, 50]
player = pygame.Surface(player_Size)
player_pos = [50, 50]
move_speed = [0, 0]
speed = 3

inventario = {}


def game():
    start = True
    while start:
        Display.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    move_speed[0] = speed
                if event.key == K_LEFT:
                    move_speed[0] = -speed
                if event.key == K_DOWN:
                    move_speed[1] = speed
                if event.key == K_UP:
                    move_speed[1] = -speed
            if event.type == KEYUP:
                if event.key == K_RIGHT and move_speed[0] == speed or event.key == K_LEFT and move_speed[0] == -speed:
                    move_speed[0] = 0
                if event.key == K_UP and move_speed[1] == -speed or event.key == K_DOWN and move_speed[1] == speed:
                    move_speed[1] = 0

        player_pos[0] += move_speed[0]
        player_pos[1] += move_speed[1]

        Display.blit(player, player_pos)

        Clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    game()
