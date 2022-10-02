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

Display_Size = [600, 500]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

cenario = {'grama_e': pygame.image.load('images/grama_e.png').convert(), 'grama': pygame.image.load('images/grama.png').convert(),
           'grama_d': pygame.image.load('images/grama_d.png').convert(), 'terra': pygame.image.load('images/terra.png').convert(),
           'canto': pygame.image.load('images/canto.png').convert(), 'remover': pygame.image.load('images/remover.png').convert()}

mapa = []

f = open('mapa_base.txt', 'r')
arq = f.read()
f.close()
arq = arq.split('\n')
for item in arq:
    mapa.append(item)

x = 10
y = 10
sprites = []
for img in cenario.values():
    tam = img.get_rect()
    tam.x = x
    tam.y = y
    sprites.append([pygame.Rect(tam), img])
    x += tam.width + 10


def map_making():
    scroll = [0, 0]
    spd_scroll = 5
    scroll_move = [0, 0]
    mostrar = []
    select = ''
    maior = 0
    while True:
        Display.fill((100, 100, 100))

        pintar = True
        mostrou = False

        scroll[0] += scroll_move[0]
        scroll[1] += scroll_move[1]

        for mostrado in mostrar:
            mostrado[1][0] -= scroll_move[0]
            mostrado[1][1] -= scroll_move[1]

        for img in sprites:
            Display.blit(img[1], img[0])

        escrever(Display, str(int(Clock.get_fps())), 20, (255, 255, 255), (0, 0))

        mapa_col = []
        y = 1
        for camada in mapa:
            x = 0
            for linha in camada:
                posição = pygame.Rect(x * 32 - scroll[0], y * 32 - scroll[1], 32, 32)
                if -32 < posição[0] < Display_Size[0] and -32 < posição[1] < Display_Size[1]:
                    mapa_col.append(posição)
                    if len(mostrar) > 0:
                        for mostrado in mostrar:
                            if mostrado[1] == posição:
                                Display.blit(mostrado[0], posição)
                if x == 48:
                    maior = x * 32
                if linha == '1':
                    Display.blit(cenario['terra'], posição)
                x += 1
            y += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    scroll_move[0] = spd_scroll
                if event.key == K_LEFT or event.key == K_a:
                    scroll_move[0] = -spd_scroll
                if event.key == K_DOWN or event.key == K_s:
                    scroll_move[1] = spd_scroll
                if event.key == K_UP or event.key == K_w:
                    scroll_move[1] = -spd_scroll

            if event.type == KEYUP:
                if (event.key == K_RIGHT or event.key == K_d) and scroll_move[0] == spd_scroll\
                        or (event.key == K_LEFT or event.key == K_a) and scroll_move[0] == -spd_scroll:
                    scroll_move[0] = 0
                if (event.key == K_DOWN or event.key == K_s) and scroll_move[1] == spd_scroll\
                        or (event.key == K_UP or event.key == K_w) and scroll_move[1] == -spd_scroll:
                    scroll_move[1] = 0

                if event.key == K_RETURN:
                    salvar_mapa(maior, mostrar, scroll)

            if event.type == MOUSEBUTTONUP:
                if event.button == BUTTON_LEFT:
                    mouse = pygame.mouse.get_pos()
                    mouse_col = pygame.Rect(mouse[0], mouse[1], 1, 1)
                    for col in sprites:
                        if mouse_col.colliderect(col[0]):
                            pintar = False
                            for img in cenario.values():
                                if col[1] == img:
                                    select = img

                    if mouse_col.y > 72:
                        if select != '' and select != cenario['remover'] and pintar:
                            for tile in mapa_col:
                                if mouse_col.colliderect(tile):
                                    if len(mostrar) > 0:
                                        for ja in mostrar:
                                            if tile == ja[1]:
                                                mostrou = True
                                    if not mostrou:
                                        if [select, tile] not in mostrar:
                                            mostrar.append([select, tile])

                    if select == cenario['remover']:
                        for tile in mostrar:
                            if mouse_col.colliderect(tile[1]):
                                mostrar.remove(tile)

                if event.button == BUTTON_RIGHT:
                    if select != '':
                        select = pygame.transform.rotate(select, -90)

        if select != '':
            Display.blit(select, (Display_Size[0] - 42, 10))

        pygame.display.update()
        Clock.tick(120)


def salvar_mapa(maior, mostrar, scroll):
    mapa_final = []
    y = 1
    for camada in mapa:
        x = 0
        for linha in camada:
            num = '0'
            posição = pygame.Rect(x * 32 - scroll[0], y * 32 - scroll[1], 32, 32)
            if len(mostrar) > 0:
                for mostrado in mostrar:
                    if mostrado[1] == posição:
                        b = 1
                        for sprit in cenario.values():
                            if mostrado[0] == sprit:
                                num = str(b)
                            b += 1
            mapa_final.append([posição, num])
            x += 1
        y += 1

    fim = []
    maior -= scroll[0]
    for pos in mapa_final:
        resultado = pos[1]
        if pos[0][0] == maior:
            resultado = resultado + '\n'

        fim.append(resultado)

    f = open('texto.txt', 'w')
    for item in fim:
        f.write(item)
    f.close()
    return


if __name__ == '__main__':
    map_making()



