import pygame
from pygame.locals import *
from random import randint
from time import sleep

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

window_width = 800
window_height = 600

Clock = pygame.time.Clock()
pygame.init()
tela = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Jogo')


def desviou(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render(f'Desviou: {count}', True, preto)
    tela.blit(text, (10, 1))


def personagem(x, y):
    # perso = pygame.Surface((32, 32))
    perso = pygame.image.load('Sem título.png')
    # perso.fill(branco)
    tela.blit(perso, (x, y))


def inimigos(iniX, iniY, iniW, iniH, color):
    pygame.draw.rect(tela, color, [iniX, iniY, iniW, iniH])


def bordas():
    chao = pygame.Surface((window_width, 30))
    chao.fill((50, 200, 50))
    tela.blit(chao, (0, 570))
    paredes = pygame.Surface((5, window_height))
    paredes.fill((200, 0, 0))
    tela.blit(paredes, (0, 0))
    tela.blit(paredes, (795, 0))


def Game_loop():
    gravidade = 3
    velocidade = 5
    x_move = 0
    y_move = gravidade
    x = 384
    y = 538
    iniX = [randint(11, 790)]
    iniY = [-300]
    queda = 8
    iniW = 50
    iniH = 50
    pulo = 0
    contagem = 0
    Sair = False
    while not Sair:

        if iniX[0] + iniW > window_width - 10:
            iniX[0] -= iniX[0] + iniW - window_width

        if pulo < 20:
            pulo += 1

        if y >= 538:
            y -= y_move

        if x < 10 or x + 18 > 790:
            Game_loop()
        if y < iniY[0] + iniH and y + 18 > iniY[0]:
            if iniX[0] < x < iniX[0] + iniW or iniX[0] < x + 18 < iniX[0] + iniW:
                Game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_move = velocidade
                if event.key == pygame.K_LEFT:
                    x_move = -velocidade
                if event.key == pygame.K_UP and pulo > 19:
                    pulo = 0
                    y_move = -velocidade
                if event.key == pygame.K_DOWN:
                    y_move = velocidade

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = gravidade

        x += x_move
        y += y_move

        iniY[0] += queda

        Clock.tick(60)
        tela.fill((220, 220, 255))

        desviou(contagem)
        personagem(x, y)
        bordas()
        inimigos(iniX[0], iniY[0], iniW, iniH, preto)

        if iniY[0] > 700:
            contagem += 1
            if contagem > 1:
                iniH += 1
                iniW += 3
                queda += 0.2
                for c in range(0, 2):
                    iniY[c] = -20 - iniH
                    iniX[c] = randint(11, 774)
            else:
                iniX.append([])
                iniY.append([])


        pygame.display.update()


Game_loop()
pygame.quit()
