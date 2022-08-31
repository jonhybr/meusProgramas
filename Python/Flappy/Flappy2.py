import pygame
from pygame.locals import *


pygame.init()
Display_Size = [500, 400]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()
pontuação = 0

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




def main():
    start_screen()
    while True:
        game_loop()
        game_over()


def start_screen():
    while True:
        check_exit()
        Display.fill((0, 0, 0))
        for event in pygame.event.get(KEYUP):
            if event.key == K_UP:
                return
        escrever(Display, 'Flappy2', 80, (50, 150, 50), cppos='middle', surface_size=Display_Size, antialias=True)
        escrever(Display, 'Press Up Arrow to start',  25, (80, 80, 80), (155, 300), antialias=True)
        pygame.display.update()
        Clock.tick(30)


def game_loop():
    global pontuação
    pontuação = 0
    flappy = desenhar((32, 32), (150, 30, 30))
    flappy_pos = [120, 168]
    queda = 0
    bateu = False
    cano = desenhar((30, 300), (50, 180, 50))
    canos_pos = [300, -150]
    aleatorio = []
    start = False
    while True:
        Display.fill((130, 130, 180))
        check_exit()

        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_UP:
                    start = True
                    queda = 0
                    for c in range(0, 10):
                        queda -= 1

        if flappy_pos[1] + 32 > Display_Size[1] or flappy_pos[1] < 0:
            break

        if start:
            if queda != 6:
                queda += 1
            flappy_pos[1] += queda
            canos_pos[0] -= 3

        if bateu:
            break
        bateu = False

        if flappy_pos[0] == canos_pos[0]:
            pontuação += 1

        x = 0
        for filheira in range(0, 3):
            y = 0
            if len(aleatorio) < 3:
                numero = random(-100, 100)
                aleatorio.append(numero)
            for linha in range(0, 2):
                canospos = [canos_pos[0] + x, canos_pos[1] + y + aleatorio[filheira]]
                Display.blit(cano, (canospos[0], canospos[1]))
                y += 390
                if flappy_pos[0] + 32 > canospos[0] and flappy_pos[0] < canospos[0] + 30\
                        and flappy_pos[1] + 32 > canospos[1] and flappy_pos[1] < canospos[1] + 300:
                    bateu = True
            if filheira == 2 and canos_pos[0] + 30 < 0:
                canos_pos[0] += 180
                del aleatorio[0]
            x += 180

        escrever(Display, f'Pontos: {pontuação}', 20, (255, 255, 255), (5, 5), antialias=True)
        Display.blit(flappy, flappy_pos)
        pygame.display.update()
        Clock.tick(30)


def game_over():
    global pontuação
    while True:
        check_exit()
        for event in pygame.event.get(KEYUP):
            if event.key == K_RETURN:
                return
        Display.fill((0, 0, 0))
        escrever(Display, 'Game Over!', 50, (150, 50, 50), cppos='middle', surface_size=Display_Size, antialias=True)
        escrever(Display, f'Pontuação: {pontuação}', 30, (80, 80, 80), (180, 300), antialias=True)
        pygame.display.update()
        Clock.tick(30)


if __name__ == '__main__':
    main()
