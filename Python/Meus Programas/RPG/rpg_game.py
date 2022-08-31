import pygame
from pygame.locals import *

pygame.init()
SCREEN_SIZE = (500, 400)
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
FPS = pygame.time.Clock()

try:
    f = open('player.txt', 'r')
    arq = f.read()

except ValueError:
    f = open('player.txt', 'w')

except FileNotFoundError:
    f = open('player.txt', 'w')


try:
    f = open('mapa.txt', 'r')
    arq = f.read()

except ValueError:
    f = open('mapa.txt', 'w')

except FileNotFoundError:
    f = open('mapa.txt', 'w')


def img_load(sprite):
    img = pygame.image.load('sprites2/' + sprite).convert()
    img = pygame.transform.scale2x(img)
    return img


sprites = {'grama': img_load('grama.png'), 'terra': img_load('terra.png'), 'terra_e': img_load('terra_e.png'),
           'terra_c': img_load('terra_c.png'), 'terra_d': img_load('terra_d.png'), 'terra_b': img_load('terra_b.png'),
           'grama_ce': img_load('grama_ce.png'), 'grama_cd': img_load('grama_cd.png'),
           'grama_be': img_load('grama_be.png'), 'grama_bd': img_load('grama_bd.png'),
           'agua': img_load('agua.png'), 'agua_ce': img_load('agua_ce.png'), 'agua_cd': img_load('agua_cd.png'),
           'agua_be': img_load('agua_be.png'), 'agua_bd': img_load('agua_bd.png'), 'agua_e': img_load('agua_e.png'),
           'agua_c': img_load('agua_c.png'), 'agua_d': img_load('agua_d.png'), 'agua_b': img_load('agua_b.png'),
           'casa_be': img_load('casa_be.png'), 'casa_b': img_load('casa_b.png'), 'casa_bd': img_load('casa_bd.png'),
           'casa_e': img_load('casa_e.png'), 'casa_d': img_load('casa_d.png'), 'casa_m': img_load('casa_m.png'),
           'teto': img_load('teto.png')}


def game():
    SCREEN.fill((100, 100, 100))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()

        FPS.tick(60)
        pygame.display.update()


game()