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

