import pygame
from pygame.locals import *
from random import randint
from time import sleep

pygame.init()
Display_Width = 800
Display_Height = 600
Display_Size = (Display_Width, Display_Height)
Display = pygame.display.set_mode(Display_Size)
clock = pygame.time.Clock()


def personagem(px, py):
    s_perso = pygame.Surface((32, 32))
    Display.blit(s_perso, (px, py))


def sair():
    Textfont = pygame.font.Font('freesansbold.ttf', 32)
    TextTexto = Textfont.render('Você não pode sair!', True, (0, 0, 0), None)
    TextLocal = TextTexto.get_rect()
    TextLocal.center = (Display_Width / 2, Display_Height / 2)
    Display.blit(TextTexto, TextLocal)


def tiros(tx, ty):
    s_tiro = pygame.Surface((20, 20))
    Display.blit(s_tiro, (tx, ty))


def Game_loop():
    px = 32
    py = 568
    x_move = 0
    y_move = 0
    gravidade = 12
    count = 0
    while True:

        print(x_move, y_move, px, py)
        ground = False
        px += x_move
        py += y_move
        py += gravidade
        movimento = 6
        count += 1

        if gravidade != 12:
            gravidade += 1

        if py + 32 > 600:
            ground = True
            py -= gravidade

        if px < 0:
            px += movimento
        if px + 32 > 800:
            px -= movimento

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    x_move = movimento
                if event.key == K_LEFT:
                    x_move = -movimento
                if event.key == K_LSHIFT:
                    if x_move == movimento:
                        x_move = movimento + 3
                    if x_move == -movimento:
                        x_move = -movimento - 3
                if event.key == K_UP:
                    if ground:
                        if x_move == 0:
                            y_move = 1
                            for c in range(0, 200):
                                Display.fill((110, 110, 150))
                                personagem(px, py)
                                pygame.display.update()
                                py -= y_move
                            y_move = 0
                            gravidade = 0
                        if x_move == movimento:
                            x_move = 0.6
                            y_move = 1
                            for c in range(0, 180):
                                Display.fill((110, 110, 150))
                                personagem(px, py)
                                pygame.display.update()
                                py -= y_move
                                px += x_move
                                if px + 32 > 800:
                                    px -= movimento
                            y_move = 0
                            px = px // 1
                            x_move = movimento
                            gravidade = 0
                        if x_move == -movimento:
                            x_move = 0.6
                            y_move = 1
                            for c in range(0, 180):
                                Display.fill((110, 110, 150))
                                personagem(px, py)
                                pygame.display.update()
                                py -= y_move
                                px -= x_move
                                if px < 0:
                                    px += movimento
                            y_move = 0
                            px = px // 1
                            x_move = -movimento
                            gravidade = 0

            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_LEFT:
                    x_move = 0
                if event.key == K_LSHIFT:
                    if x_move > 0:
                        x_move = movimento
                    if x_move < 0:
                        x_move = -movimento

        clock.tick(60)
        Display.fill((110, 110, 150))

        if px <= 10 or px + 32 >= 790:
            sair()

        personagem(px, py)
        pygame.display.update()


Game_loop()
