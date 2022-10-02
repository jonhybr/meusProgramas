import pygame
from pygame.locals import *

import pygame
from pygame.locals import *
from random import randint


def escrever(surface,texto,tam=32,cor=(0, 0, 0),tpos=(0, 0),cppos='',surface_size=(),negrito=None, italico=None, antialias=False,background=None):
    fonte = pygame.font.SysFont(None, tam, negrito, italico)
    text = fonte.render(texto, antialias, cor, background)
    if not cppos == '':
        centro = text.get_rect()
        if cppos == 'middle':
            centro.center = (surface_size[0] // 2 + tpos[0], surface_size[1] // 2 + tpos[1])
        return surface.blit(text, centro)
    return surface.blit(text, tpos)


def escreve(texto, tam=32, cor=(0, 0, 0), antialias=False):
    font = pygame.font.Font(None, tam)
    text = font.render(texto, antialias, cor)
    pos = text.get_rect()
    return text, pos


def terminate():
    pygame.quit()
    quit()


def check_exit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


def desenhar(tam=(32, 32), cor=(0, 0, 0), image=False, imagem='imagem.png'):
    if image:
        desenho = pygame.image.load(imagem)
    else:
        desenho = pygame.Surface(tam)
        desenho.fill(cor)
    return desenho


def random(ini=1, fim=100):
    numero = randint(ini, fim)
    return numero




pygame.init()
Display_size = (400, 500)
Display = pygame.display.set_mode(Display_size)
Clock = pygame.time.Clock()

grama = pygame.Surface((32, 32))

colisoes = []
mapa = [['1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
       ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1'],
       ['1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1'],
       ['1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1'],
       ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1'],
       ['1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
       ['1', '0', '1', '0', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1'],
       ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
       ['0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0'],
       ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1', '1', '1', '0', '1', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1'],
       ['1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
       ['1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1'],
       ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1'],
       ['1', '1', '1', '0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1'],
       ['1', '2', '1', '0', '1', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '1', '0', '1', '0', '1'],
       ['1', '2', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1'],
       ['1', '2', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

moedas = []
moeda = desenhar((8, 8), (200, 200, 200))
gerar_moedas = True
moeda_col = moeda.get_rect()
pegou = []

pac = desenhar((20, 20), (200, 200, 10))
pac_col = pac.get_rect()
pac_col.x = 20
pac_col.y = 460
move = 10
movex = movey = 0
vel = 20

pontuação = 0
moving = False

while True:
    Display.fill((20, 20, 60))

    Display.blit(pac, (pac_col.x, pac_col.y))
    escrever(Display, f'Score: {pontuação}', 20, (255, 255, 255), (10, 10))

    y = 80
    for camada in mapa:
        x = 0
        for linha in camada:
            if linha == '1':
                Display.blit(grama, (x, y))
                parede_col = grama.get_rect(x=x, y=y)
                if parede_col not in colisoes:
                    colisoes.append(parede_col)
            if linha == '0':
                if gerar_moedas:
                    if [x, y] not in moedas:
                        moedas.append([x, y])
            x += 20
        y += 20

    gerar_moedas = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            moving = True
            movey = 0
            movex = 0
            if event.key == K_RIGHT:
                movex = vel
            if event.key == K_DOWN:
                movey = vel
            if event.key == K_LEFT:
                movex = -vel
            if event.key == K_UP:
                movey = -vel
    if moving:
        move += 1
        if move >= 8:
            pac_col.x += movex
            for colisao in colisoes:
                if pac_col.colliderect(colisao):
                    if movex > 0:
                        pac_col.right = colisao.left
                    if movex < 0:
                        pac_col.left = colisao.right
            pac_col.y += movey
            for colisao in colisoes:
                if pac_col.colliderect(colisao):
                    if movey > 0:
                        pac_col.bottom = colisao.top
                    if movey < 0:
                        pac_col.top = colisao.bottom
            move = 0

    if pac_col.y > Display_size[1] - 20:
        pac_col.y = 80
    if pac_col.y < 80:
        pac_col.y = 480
    if pac_col.x < 0:
        pac_col.x = 380
    if pac_col.x > 380:
        pac_col.x = 0

    for moe in range(0, len(moedas)):
        Display.blit(moeda, (moedas[moe][0] + 6, moedas[moe][1] + 6))
        moeda_col.x = moedas[moe][0]
        moeda_col.y = moedas[moe][1]
        if pac_col.colliderect(moeda_col):
            pontuação += 10
            pegou.append(moe)

    for coin in pegou:
        moedas.pop(coin)
        pegou.clear()

    pygame.display.update()
    Clock.tick(60)
