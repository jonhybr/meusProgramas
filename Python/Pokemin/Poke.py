import pygame
from pygame.locals import *


pygame.init()

Display_Size = [500, 500]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

menu = pygame.image.load('menu_poke.png')

barra_vida = pygame.Surface((10, 15))
barra_vida.fill((190, 50, 50))

personagem = {'Nivel': 1, 'Nome': 'Geraldo', 'Atk': 1, 'Def': 1, 'Vida': 20, 'Velocidade': 5}
geraldo = pygame.image.load('Geraldo.png')
vida_max_perso = personagem['Vida']

monstros = [{'Nivel': 1, 'Nome': 'Slime', 'Atk': 2, 'Def': 0, 'Vida': 20, 'Velocidade': 3, 'Img': pygame.image.load('Slime.png')},
            {'Nivel': 1, 'Nome': 'Aguia', 'Atk': 3, 'Def': 0, 'Vida': 15, 'Velocidade': 6, 'Img': pygame.image.load('Aguia.png')}]

lista_ataques = {'Soco': {'Nome': 'Soco', 'Dano': 2, 'Usos':   25},
                 'Mordida': {'Nome': 'Mordida', 'Dano': 5, 'Usos': 10}}

opções = ['Lutar', 'Trocar', 'Item', 'Fugir']
op_col = []

ataques = [lista_ataques['Soco'].copy(), lista_ataques['Mordida'].copy()]
atk_col = []

vida_max = monstros[0]['Vida']

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




def game_loop():
    while True:
        Display.fill((220, 220, 220))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        Clock.tick(60)
        pygame.display.update()


def batalha():
    global menu
    menu_inicial = True
    while True:
        check_exit()
        Display.fill((100, 100, 100))

        Display.blit(pygame.image.load('cenario_temp.png'), (0, 0))
        Display.blit(menu, (0, 340))

        if menu_inicial:
            menu = pygame.image.load('menu_poke.png')
        else:
            menu = pygame.image.load('menu_poke_fight.png')

        Display.blit(pygame.transform.scale(geraldo, (128, 128)), (310, 170))

        x = 0
        for vida in range(0, 20):
            div_monst = vida_max / 20
            if div_monst * vida < monstros[0]['Vida']:
                Display.blit(barra_vida, (20 + x, 20))
            else:
                Display.blit(pygame.Surface((10, 15)), (20 + x, 20))

            div_jogad = vida_max_perso / 20
            if div_jogad * vida < personagem['Vida']:
                Display.blit(barra_vida, (280 + x, 290))
            else:
                Display.blit(pygame.Surface((10, 15)), (280 + x, 290))
            x += 10

        nome_monstro = escreve(monstros[0]['Nome'] + ' Lvl ' + str(monstros[0]['Nivel']), 20, (255, 255, 255), True)
        nome_monstro[1].bottomleft = (20, 20)
        Display.blit(nome_monstro[0], nome_monstro[1])
        vida_monstro = escreve(str(monstros[0]['Vida']), 20, (255, 255, 255), True)
        vida_monstro[1].center = (120, 20 + 15 // 2)
        Display.blit(vida_monstro[0], vida_monstro[1])

        nome_perso = escreve(personagem['Nome'] + ' Lvl ' + str(personagem['Nivel']), 20, (255, 255, 255), True)
        nome_perso[1].bottomleft = (280, 290)
        Display.blit(nome_perso[0], nome_perso[1])
        vida_perso = escreve(str(personagem['Vida']), 20, (255, 255, 255), True)
        vida_perso[1].center = (380, 290 + 15 // 2)
        Display.blit(vida_perso[0], vida_perso[1])

        if monstros[0]['Vida'] <= 0 or personagem['Vida'] <= 0:
            break

        Display.blit(pygame.transform.scale(monstros[0]['Img'], (128, 128)), (60, 60))

        if menu_inicial:
            x = 294
            y = 382
            for op in range(0, 4):
                if op == len(opções) // 2:
                    x = 294
                    y += 56
                if [x, y, x + 70, y + 28, op] not in op_col:
                    op_col.append([x, y, x + 70, y + 28, op])
                es = escreve(opções[op], 20, (255, 255, 255), True)
                es[1].center = (x + 35, y + 14)
                Display.blit(es[0], es[1])
                x += 98

        if not menu_inicial:
            x = 49
            y = 382
            for atk in ataques:
                if len(ataques) >= 3 and atk == ataques[2]:
                    y = 438
                    x = 49
                if [x, y, x + 70, y + 28, atk] not in atk_col:
                    atk_col.append([x, y, x + 70, y + 28, atk['Nome']])
                es = escreve(atk['Nome'], 20, (255, 255, 255), True)
                es[1].center = (x + 35, y + 14)
                Display.blit(es[0], es[1])
                x += 98

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if event.button == BUTTON_LEFT:
                    if menu_inicial:
                        for opc in op_col:
                            if opc[0] < mouse[0] < opc[2] and opc[1] < mouse[1] < opc[3]:
                                if opc[4] == 0:
                                    menu_inicial = False
                                if opc[4] == 3:
                                    pygame.quit()
                    if not menu_inicial:
                        for ata in atk_col:
                            if ata[0] < mouse[0] < ata[2] and ata[1] < mouse[1] < ata[3]:
                                if personagem['Velocidade'] > monstros[0]['Velocidade']:
                                    if ata[4] == ataques[0]['Nome']:
                                        monstros[0]['Vida'] -= ataques[0]['Dano']
                                    if ata[4] == ataques[1]['Nome']:
                                        monstros[0]['Vida'] -= ataques[1]['Dano']
                                    personagem['Vida'] -= monstros[0]['Atk']
                                else:
                                    personagem['Vida'] -= monstros[0]['Atk']
                                break

                if event.button == BUTTON_RIGHT:
                    if not menu_inicial:
                        menu_inicial = True

        Clock.tick(60)
        pygame.display.update()


batalha()
