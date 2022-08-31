import pygame
from pygame.locals import *

pygame.init()

Display_Size = [512, 512]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()
chao = pygame.image.load('assets/Tile_1.png')
parede = pygame.image.load('assets/Tile_2.png')
flecheiro = pygame.image.load('assets/Tile_armadilha.png')
flecha = pygame.image.load('assets/Flecha.png')
particulas = pygame.image.load('assets/Particulas.png')
porta_trancada_ama = pygame.image.load('assets/Porta_trancada_3.png')
porta_trancada_cin = pygame.image.load('assets/Porta_trancada_2.png')
chave_ama = pygame.image.load('assets/Chave_ama.png')
chave_cin = pygame.image.load('assets/Chave_cin.png')

nivel = 1

mapa = '0'

mapa1 = [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '99', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['5', '0', '0', '0', '0', '0', '0', '6', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

mapa2 = [['1', '2', '1', '2', '1', '2', '1', '2', '1', '1', '2', '1', '2', '1', '2', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '2'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '2'],
        ['2', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '0', '0', '0', '2'],
        ['1', '0', '1', '2', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1', '1', '1', '0', '1', '0', '1', '0', '0', '0', '2'],
        ['1', '0', '1', '0', '0', '1', '0', '0', '0', '1', '0', '1', '1', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1', '0', '6', '0', '1', '0', '0', '1', '99', '0', '1'],
        ['1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1'],
        ['1', '0', '0', '1', '0', '1', '1', '1', '1', '1', '0', '1', '1', '1', '2', '1'],
        ['1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '2', '1', '1', '1', '1'],
        ['5', '0', '0', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

mapa3 = [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '2', '2', '1', '1', '1', '0', '8', '0', '1'],
         ['1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1'],
         ['2', '0', '0', '0', '1', '0', '0', '0', '0', '0', '2', '1', '0', '0', '0', '1'],
         ['1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', '1', '1'],
         ['1', '2', '1', '2', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '2'],
         ['1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
         ['1', '0', '1', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1'],
         ['1', '0', '1', '0', '1', '0', '0', '1', '1', '0', '0', '1', '1', '1', '1', '1'],
         ['1', '0', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '2', '1', '1', '1'],
         ['1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1'],
         ['1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '7', '0', '0', '0', '1'],
         ['5', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '6', '0', '1'],
         ['1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
         ['1', '1', '1', '1', '1', '1', '1', '2', '2', '1', '1', '1', '1', '1', '1', '1']]


def game_loop():
    global mapa, nivel

    if nivel == 1:
        mapa = mapa1
    if nivel == 2:
        mapa = mapa2
    if nivel == 3:
        mapa = mapa3

    move = 12
    colisao = []
    coletaveis = []
    armadilhas = []
    piso = []
    flechas = []
    flecha_spd = 2

    jogador = pygame.Surface((32, 32))
    jogador_pos = [32, 32]
    movimento = 0
    spawn = True

    pegou_chave_ama = False
    pegou_chave_cin = False

    while True:
        Display.fill((100, 100, 100))

        if move >= 12:
            if movimento == 'right':
                jogador_pos[0] += 32
                move = 0
            if movimento == 'left':
                jogador_pos[0] -= 32
                move = 0
            if movimento == 'up':
                jogador_pos[1] -= 32
                move = 0
            if movimento == 'down':
                jogador_pos[1] += 32
                move = 0
        else:
            move += 1

        y = 0
        for linha in mapa:
            x = 0
            for pos in linha:
                if spawn and pos == '99':
                    jogador_pos = [x, y]
                    spawn = False
                if pos == '0' or pos == '6' or pos == '8' or pos == '99':
                    Display.blit(chao, (x, y))
                    if [x, y] not in piso:
                        piso.append([x, y])
                if pos == '1':
                    Display.blit(parede, (x, y))
                    if [x, y] not in colisao:
                        colisao.append([x, y])
                if pos == '2':
                    if [x, y] not in colisao and [x, y] not in armadilhas:
                        colisao.append([x, y])
                        armadilhas.append({'Pos_Arm': [x, y], 'Dir': ''})
                if pos == '5' and {'Nome': 'porta_ama', 'Pos': [x, y]} not in coletaveis:
                    coletaveis.append({'Nome': 'porta_ama', 'Pos': [x, y]})
                if pos == '6' and {'Nome': 'chave_ama', 'Pos': [x, y]} not in coletaveis:
                    coletaveis.append({'Nome': 'chave_ama', 'Pos': [x, y]})
                if pos == '7' and {'Nome': 'porta_cin', 'Pos': [x, y]} not in coletaveis:
                    coletaveis.append({'Nome': 'porta_cin', 'Pos': [x, y]})
                if pos == '8' and {'Nome': 'chave_cin', 'Pos': [x, y]} not in coletaveis:
                    coletaveis.append({'Nome': 'chave_cin', 'Pos': [x, y]})
                x += 32
            y += 32

        for get in coletaveis:
            if get['Nome'] == 'chave_ama' and not pegou_chave_ama:
                Display.blit(chave_ama, get['Pos'])
                if get['Pos'] == jogador_pos:
                    pegou_chave_ama = True

            if get['Nome'] == 'porta_ama':
                Display.blit(porta_trancada_ama, get['Pos'])
                if get['Pos'] not in colisao and not pegou_chave_ama:
                    colisao.append(get['Pos'])
                if get['Pos'] in colisao and pegou_chave_ama:
                    colisao.remove(get['Pos'])

            if get['Nome'] == 'chave_cin':
                if not pegou_chave_cin:
                    Display.blit(chave_cin, get['Pos'])
                if jogador_pos == get['Pos']:
                    pegou_chave_cin = True

            if get['Nome'] == 'porta_cin':
                Display.blit(porta_trancada_cin, get['Pos'])
                if get['Pos'] not in colisao and not pegou_chave_cin:
                    colisao.append(get['Pos'])
                if get['Pos'] in colisao and pegou_chave_cin:
                    colisao.remove(get['Pos'])

        if len(armadilhas) > 0:
            for flechada in flechas:
                if flechada['Dir'] == 'right':
                    Display.blit(pygame.transform.rotate(flecha, 180), flechada['Pos'])
                    flechada['Pos'][0] += flecha_spd
                if flechada['Dir'] == 'left':
                    Display.blit(flecha, flechada['Pos'])
                    flechada['Pos'][0] -= flecha_spd
                if flechada['Dir'] == 'up':
                    Display.blit(pygame.transform.rotate(flecha, -90), flechada['Pos'])
                    flechada['Pos'][1] -= flecha_spd
                if flechada['Dir'] == 'down':
                    Display.blit(pygame.transform.rotate(flecha, 90), flechada['Pos'])
                    flechada['Pos'][1] += flecha_spd

                if jogador_pos[0] + 32 > flechada['Pos'][0] and jogador_pos[0] < flechada['Pos'][0] + 32\
                        and jogador_pos[1] + 32 > flechada['Pos'][1] and jogador_pos[1] < flechada['Pos'][1] + 32:
                    return

                for colid in colisao:
                    if flechada['Dir'] == 'right' and [flechada['Pos'][0] + 16, flechada['Pos'][1]] == colid:
                        flechada['Pos'] = flechada['Spawn'].copy()
                    if flechada['Dir'] == 'left' and [flechada['Pos'][0] - 16, flechada['Pos'][1]] == colid:
                        flechada['Pos'] = flechada['Spawn'].copy()
                    if flechada['Dir'] == 'up' and [flechada['Pos'][0], flechada['Pos'][1] - 16] == colid:
                        flechada['Pos'] = flechada['Spawn'].copy()
                    if flechada['Dir'] == 'down' and [flechada['Pos'][0], flechada['Pos'][1] + 16] == colid:
                        flechada['Pos'] = flechada['Spawn'].copy()

            for armadilha in armadilhas:
                direct = ''

                for space in piso:
                    if [armadilha['Pos_Arm'][0], armadilha['Pos_Arm'][1] - 32] == space:
                        direct = 'up'
                        Display.blit(pygame.transform.rotate(flecheiro, -90), armadilha['Pos_Arm'])
                        break
                    if [armadilha['Pos_Arm'][0] - 32, armadilha['Pos_Arm'][1]] == space:
                        direct = 'left'
                        Display.blit(flecheiro, armadilha['Pos_Arm'])
                        break
                    if [armadilha['Pos_Arm'][0] + 32, armadilha['Pos_Arm'][1]] == space:
                        direct = 'right'
                        Display.blit(pygame.transform.rotate(flecheiro, 180), armadilha['Pos_Arm'])
                        break
                    if [armadilha['Pos_Arm'][0], armadilha['Pos_Arm'][1] + 32] == space:
                        direct = 'down'
                        Display.blit(pygame.transform.rotate(flecheiro, 90), armadilha['Pos_Arm'])
                        break

                if len(flechas) < len(armadilhas):
                    flechas.append({'Pos': armadilha['Pos_Arm'].copy(), 'Dir': direct, 'Spawn': armadilha['Pos_Arm'].copy()})

        for col in colisao:
            if movimento == 'right' and jogador_pos == col:
                jogador_pos[0] -= 32
            if movimento == 'left' and jogador_pos == col:
                jogador_pos[0] += 32
            if movimento == 'up' and jogador_pos == col:
                jogador_pos[1] += 32
            if movimento == 'down' and jogador_pos == col:
                jogador_pos[1] -= 32

        if pegou_chave_ama:
            for colet in coletaveis:
                if colet['Nome'] == 'porta_ama' and colet['Pos'] == jogador_pos:
                    nivel += 1
                    return

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    movimento = 'right'
                if event.key == K_LEFT:
                    movimento = 'left'
                if event.key == K_UP:
                    movimento = 'up'
                if event.key == K_DOWN:
                    movimento = 'down'
            if event.type == KEYUP:
                if event.key == K_RIGHT and movimento == 'right' or event.key == K_LEFT and movimento == 'left' \
                        or event.key == K_UP and movimento == 'up' or event.key == K_DOWN and movimento == 'down':
                    movimento = ''
                if event.key == K_RETURN:
                    if nivel == 3:
                        nivel -= 2
                    else:
                        nivel += 1
                    return
            if event.type == QUIT:
                pygame.quit()
                quit()

        Display.blit(jogador, jogador_pos)

        pygame.display.update()
        Clock.tick(60)


while True:
    game_loop()
