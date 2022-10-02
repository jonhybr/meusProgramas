import pygame
from pygame.locals import *
from random import randint

pygame.init()

Game_Display_Size = [160, 500]
Game_Display = pygame.Surface(Game_Display_Size)
Display_Size = [350, 500]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

s = [['0', '0', '0'],
     ['0', '1', '1'],
     ['1', '1', '0']]

z = [['0', '0', '0'],
     ['1', '1', '0'],
     ['0', '1', '1']]

l = [['0', '1', '0'],
     ['0', '1', '0'],
     ['0', '1', '1']]

r = [['0', '1', '0'],
     ['0', '1', '0'],
     ['1', '1', '0']]

o = [['1', '1'],
     ['1', '1']]

i = [['0', '1', '0', '0'],
     ['0', '1', '0', '0'],
     ['0', '1', '0', '0'],
     ['0', '1', '0', '0']]

t = [['0', '0', '0'],
     ['0', '1', '0'],
     ['1', '1', '1']]

blocos_sprites = [{'formato_list': s, 'img': pygame.image.load("b_verde.png"), 'grid': 3, 'formato': 's'},
                  {'formato_list': r, 'img': pygame.image.load("b_azul.png"), 'grid': 3, 'formato': 'r'},
                  {'formato_list': z, 'img': pygame.image.load("b_vermelho.png"), 'grid': 3, 'formato': 'z'},
                  {'formato_list': o, 'img': pygame.image.load("b_amarelo.png"), 'grid': 2, 'formato': 'o'},
                  {'formato_list': l, 'img': pygame.image.load("b_laranja.png"), 'grid': 3, 'formato': 'l'},
                  {'formato_list': i, 'img': pygame.image.load("b_ciano.png"), 'grid': 4, 'formato': 'i'},
                  {'formato_list': t, 'img': pygame.image.load("b_roxo.png"), 'grid': 3, 'formato': 't'}]

formato_tr = {'1': '', '2': '', '3': '',
              '4': '', '5': '', '6': '',
              '7': '', '8': '', '9': ''}

formato_qu = {'1': '', '2': '', '3': '', '4': '',
              '5': '', '6': '', '7': '', '8': '',
              '9': '', '10': '', '11': '', '12': '',
              '13': '', '14': '', '15': '', '16': ''}

bloco_atual = [5 * 16, 16, blocos_sprites[2]]
blocos_blit = []

time = 0

formato_atual = bloco_atual[2]['formato_list']

colisoes = {'left': 0, 'right': 0, 'down': 0}

caindo = 0

while True:
    Display.fill((0, 0, 0))

    ground = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        # checar teclas
        if event.type == KEYDOWN:
            if event.key == K_r:
                for sprt in blocos_sprites:
                    if bloco_atual[2]['formato'] == sprt['formato']:
                        # checar o tamanho do grid para rotacionar
                        if sprt['grid'] == 2:
                            break

                        if sprt['grid'] == 3:
                            c = 1
                            for coluna in formato_atual:
                                for linha in coluna:
                                    formato_tr[str(c)] = linha
                                    c += 1
                            formato_atual = [[formato_tr['7'], formato_tr['4'], formato_tr['1']],
                                             [formato_tr['8'], formato_tr['5'], formato_tr['2']],
                                             [formato_tr['9'], formato_tr['6'], formato_tr['3']]]

                        if sprt['grid'] == 4:
                            c = 1
                            for coluna in formato_atual:
                                for linha in coluna:
                                    formato_qu[str(c)] = linha
                                    c += 1
                            formato_atual = [[formato_qu['13'], formato_qu['9'], formato_qu['5'], formato_qu['1']],
                                             [formato_qu['14'], formato_qu['10'], formato_qu['6'], formato_qu['2']],
                                             [formato_qu['15'], formato_qu['11'], formato_qu['7'], formato_qu['3']],
                                             [formato_qu['16'], formato_qu['12'], formato_qu['8'], formato_qu['4']]]
            # mover
            if event.key == K_RIGHT:
                bloco_atual[0] += 16
                colisoes['right'] += 16
            if event.key == K_LEFT:
                bloco_atual[0] -= 16
                colisoes['left'] -= 16
            if event.key == K_DOWN:
                caindo = 8
        if event.type == KEYUP:
            if event.key == K_DOWN:
                caindo = 0

    # colisão com a tela
    if colisoes['left'] < 0:
        bloco_atual[0] += 16
    if colisoes['right'] > Game_Display_Size[0]:
        bloco_atual[0] -= 16
    if colisoes['down'] > Game_Display_Size[1]:
        bloco_atual[1] -= 16
        ground = True

    # checar colisão com peças na tela
    for p_col in bloco_atual:

        if p_col == '1':
            for col in blocos_blit:
                break


    # chegou ao chão
    if ground:
        blocos_blit.append((bloco_atual.copy(), formato_atual.copy(), player.copy()))
        bloco_atual = [5 * 16, 16, blocos_sprites[randint(0, 6)]]
        formato_atual = bloco_atual[2]['formato_list']

    # tick de movimento
    if time >= 40 and not ground:
        bloco_atual[1] += 16
        colisoes['down'] += 16
        time = 0

    # mostrar na tela
    player = []
    colisoes = {'left': 0, 'right': 0, 'down': 0}
    y = bloco_atual[1]
    for linha in formato_atual:
        x = bloco_atual[0]
        for coluna in linha:
            if coluna == '1':
                if colisoes == {'left': 0, 'right': 0, 'down': 0}:
                    colisoes['left'] = x
                    colisoes['right'] = x + 16
                    colisoes['down'] = y + 16
                if x < colisoes['left']:
                    colisoes['left'] = x
                if x + 16 > colisoes['right']:
                    colisoes['right'] = x + 16
                if y + 16 > colisoes['down']:
                    colisoes['down'] = y + 16
                player.append([x, y])
            x += 16
        y += 16

    Display.blit(Game_Display, (50, 0))
    Game_Display.fill((50, 50, 50))

    # mostrar jogador
    for pos in player:
        Game_Display.blit(pygame.transform.scale2x(bloco_atual[2]['img']), pos)

    # mostrar peças que cairam
    for bloco in blocos_blit:
        y = bloco[0][1]
        for linha in bloco[1]:
            x = bloco[0][0]
            for camada in linha:
                if camada == '1':
                    Game_Display.blit(pygame.transform.scale2x(bloco[0][2]['img']), (x, y))
                x += 16
            y += 16

    time += 1 + caindo

    Clock.tick(60)
    pygame.display.update()
