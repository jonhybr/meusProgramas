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

Display_Size = [500, 400]
Display = pygame.display.set_mode(Display_Size)

loja_Size = [Display_Size[0] - 350, Display_Size[1]]
loja = pygame.Surface(loja_Size)
loja.fill((50, 50, 50))
loja_nome = escreve('LOJA', 30, (150, 150, 150), antialias=True)
loja_nome[1].center = (loja_Size[0] // 2, 30)

opcoes = [{'Nome': 'Trabalhador', 'Preço': 5, 'DPS': 0.5, 'Quantidade': 0},
          {'Nome': 'Fazenda', 'Preço': 50, 'DPS': 2, 'Quantidade': 0},
          {'Nome': 'Fábrica', 'Preço': 250, 'DPS': 10, 'Quantidade': 0}]

click = False
Clock = pygame.time.Clock()

while True:
    check_exit()
    Display.fill((100, 100, 100))
    Display.blit(loja, (Display_Size[0] - loja_Size[0], 0))
    loja.blit(pygame.Surface((loja_Size[0], 30)), (0, 15))
    loja.blit(desenhar((loja_Size[0] - 8, Display_Size[1] - 55), (60, 60, 60)), (4, 50))
    loja.blit(loja_nome[0], loja_nome[1])

    click = False

    for event in pygame.event.get(MOUSEBUTTONUP):
        click = True

    y = 55
    for op in opcoes:
        x = 6
        opc = escreve(f"{op['Nome']}: {op['Quantidade']}", 20, (150, 150, 150), antialias=True)
        loja.blit(opc[0], (x, y))
        y += 15
        comp = escreve(f"Comprar: {op['Preço']}", 15, (150, 150, 150), antialias=True)
        loja.blit(comp[0], (x, y))
        if click:
            mouse = pygame.mouse.get_pos()
            if mouse[0] > comp[1].left and mouse[0] < comp[1].right and mouse[1] > comp[1].top and mouse[1] < comp[1].bottom:
                op['Quantidade'] += 1
        y += 20

    pygame.display.update()
    Clock.tick(60)
