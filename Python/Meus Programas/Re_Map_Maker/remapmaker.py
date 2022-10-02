import pygame
from pygame.locals import *

pygame.init()

Display_Size = (1200, 700)
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

try:
    f = open('texto.txt', 'r')
    arq = f.read()

except ValueError:
    f = open('texto.txt', 'w')

except FileNotFoundError:
    f = open('texto.txt', 'w')


def img_load(sprite):
    img = pygame.image.load('sprites/' + sprite).convert()
    img = pygame.transform.scale2x(img)
    return img


lista = ['start', 'end', 'lixeira', 'lixeira_co', 'colisao', 'porta', 'grama', 'terra', 'terra_e', 'terra_c', 'terra_d', 'terra_b', 'grama_ce', 'grama_cd', 'grama_bd',
         'grama_be', 'arbusto', 'arvore_be', 'arvore_bd', 'arvore_ce', 'arvore_cd', 'flor_rosa', 'flor_roxa', 'agua', 'agua_ce', 'agua_cd', 'agua_be',
         'agua_bd', 'agua_e', 'agua_c', 'agua_d', 'agua_b', 'casa_be', 'casa_p', 'casa_b', 'casa_j', 'casa_bd', 'casa_e', 'casa_d', 'casa_m', 'teto', 'teto2',
         'tijolo', 'parede_vertical', 'parede_horizontal', 'parede_cd', 'parede_bd', 'parede_be', 'parede_ce']

sprites = {}
for item in range(0, len(lista)):
    sprites[lista[item]] = img_load(lista[item] + '.png')

colisoes_sprites = [sprites['lixeira_co'], sprites['colisao'], sprites['porta']]


def check_pos(n1):
    while n1 % 32 != 0:
        n1 -= 1
    return n1


def map_maker():
    atual = sprites['start']
    scroll = [0, 0]
    move_scroll = [0, 0]
    startend = False
    mapa = [[0, 0], [0, 0]]
    mostras = []
    move_speed = [32, 32]
    desenhando = False
    colisoes = []
    direito = False
    while True:

        Display.fill((150, 150, 150))

        scroll[0] += move_scroll[0]
        scroll[1] += move_scroll[1]

        # mostrar os sprites

        x = 20
        sprites_col = []
        counter = 0
        pos_y = 50
        for spr in sprites.values():
            if counter % 16 == 0:
                pos_y += 40
                x = 20
                counter = 0
            pos = spr.get_rect()
            pos.x = x + scroll[0]
            pos.y = pos_y + scroll[1]
            sprites_col.append((spr, pos))
            Display.blit(spr, pos)
            x += 36
            counter += 1

        if mapa[0] != [0, 0]:
            Display.blit(sprites['start'], (mapa[0][0] + scroll[0], mapa[0][1] + scroll[1]))
        if mapa[1] != [0, 0]:
            Display.blit(sprites['end'], (mapa[1][0] + scroll[0], mapa[1][1] + scroll[1]))

        for spr in mostras:
            Display.blit(spr[0], (spr[1][0] + scroll[0], spr[1][1] + scroll[1]))
        if atual in colisoes_sprites:
            for spr in colisoes:
                Display.blit(spr[0], (spr[1][0] + scroll[0], spr[1][1] + scroll[1]))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            # teclas pressionadas
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == K_RETURN:
                    salvar_mapa(mapa, mostras, colisoes)

                # mover tela
                if event.key == K_d:
                    move_scroll[0] = -move_speed[0]
                if event.key == K_a:
                    move_scroll[0] = move_speed[0]
                if event.key == K_s:
                    move_scroll[1] = -move_speed[1]
                if event.key == K_w:
                    move_scroll[1] = move_speed[1]

            if event.type == KEYUP:
                if event.key == K_d and move_scroll[0] == -move_speed[0] or event.key == K_a and move_scroll[0] == \
                        move_speed[0]:
                    move_scroll[0] = 0
                if event.key == K_s and move_scroll[1] == -move_speed[1] or event.key == K_w and move_scroll[1] == \
                        move_speed[1]:
                    move_scroll[1] = 0
                if event.key == K_1:
                    atual = sprites_col[0][0]
                if event.key == K_2:
                    atual = sprites_col[1][0]
                if event.key == K_3:
                    atual = sprites_col[2][0]

            if event.type == MOUSEBUTTONDOWN:
                sprite = False
                if event.button == 5:
                    for col in sprites_col[::-1]:
                        if sprite:
                            atual = col[0]
                            break
                        if atual == col[0]:
                            sprite = True
                elif event.button == 4:
                    for col in sprites_col:
                        if sprite:
                            atual = col[0]
                            break
                        if atual == col[0]:
                            sprite = True

                if event.button == BUTTON_LEFT:
                    desenhando = True
                    mouse = pygame.mouse.get_pos()
                    mouse_pos = pygame.Rect((mouse[0], mouse[1], 1, 1))

                    # selecionar sprite
                    for col in sprites_col:
                        if mouse_pos.colliderect(col[1]):
                            atual = col[0]
                            desenhando = False

            if event.type == MOUSEBUTTONUP:
                if event.button == BUTTON_RIGHT:
                    direito = True
                desenhando = False

        if desenhando:
            mouse = pygame.mouse.get_pos()
            mouse_pos = pygame.Rect((mouse[0], mouse[1], 1, 1))
            if startend and atual != sprites['start'] and atual != sprites['end']:

                if mapa[0][0] + 32 + scroll[0] < mouse_pos[0] < mapa[1][0] + scroll[0] \
                        and mapa[0][1] + 32 + scroll[1] < mouse_pos[1] < mapa[1][1] + scroll[1]:

                    mouse_pos[0] = check_pos(mouse_pos[0] - scroll[0])
                    mouse_pos[1] = check_pos(mouse_pos[1] - scroll[1])

                    if direito:
                        for spr in mostras:
                            if spr[1] == mouse_pos:
                                atual = spr[0]
                                direito = False
                                break

                    # apagar
                    if atual == sprites['lixeira']:
                        for spr in mostras:
                            if spr[1] == mouse_pos:
                                mostras.remove(spr)
                                break
                    elif atual == sprites['lixeira_co']:
                        for spr in colisoes:
                            if spr[1] == mouse_pos:
                                colisoes.remove(spr)
                                break
                    # desenhar
                    else:
                        if len(mostras) == 0 and atual not in colisoes_sprites:
                            mostras.append((atual, mouse_pos))

                        desenha = True
                        if atual not in colisoes_sprites:
                            for spr in mostras:
                                if spr[1] == mouse_pos:
                                    desenha = False
                        else:
                            for spr in colisoes:
                                if spr[1] == mouse_pos:
                                    desenha = False
                        if desenha:
                            if atual not in colisoes_sprites:
                                mostras.append((atual, mouse_pos))
                            else:
                                colisoes.append((atual, mouse_pos))

            # ponto inicial e final
            if atual == sprites['start']:
                mouse_pos[0] = check_pos(mouse_pos[0])
                mouse_pos[1] = check_pos(mouse_pos[1])
                mapa[0] = (mouse_pos[0] - scroll[0], mouse_pos[1] - scroll[1])
            if atual == sprites['end']:
                mouse_pos[0] = check_pos(mouse_pos[0])
                mouse_pos[1] = check_pos(mouse_pos[1])
                mapa[1] = (mouse_pos[0] - scroll[0], mouse_pos[1] - scroll[1])
            if mapa[0] != (0, 0) and mapa[1] != (0, 0):
                startend = True

        if atual != '0':
            Display.blit(atual, (Display_Size[0] - 36, 4))

        Clock.tick(60)
        pygame.display.update()


def salvar_mapa(mapa, blocos, colisoes):
    feito = []
    # grid
    for pos_y in range(mapa[0][1] + 32, mapa[1][1], 32):
        for pos_x in range(mapa[0][0] + 32, mapa[1][0], 32):
            # checando se tem bloco
            tem = False
            for bloco in blocos:
                if pos_x == bloco[1][0] and pos_y == bloco[1][1]:
                    tem = True
                    for spr in sprites:
                        if bloco[0] == sprites[spr]:
                            feito.append(spr + ',')
            if not tem:
                feito.append('0,')
        feito.append('\n')
    feito.pop()

    f = open('texto.txt', 'w')
    for item in feito:
        f.write(item)
    f.close()

    colisoes_feito = []
    for pos_y in range(mapa[0][1] + 32, mapa[1][1], 32):
        for pos_x in range(mapa[0][0] + 32, mapa[1][0], 32):
            colidiu = False
            for col in colisoes:
                if pos_x == col[1][0] and pos_y == col[1][1]:
                    colidiu = True
                    colisoes_feito.append(str(colisoes_sprites.index(col[0])) + ',')
            if not colidiu:
                colisoes_feito.append('0,')
        colisoes_feito.append('\n')
    colisoes_feito.pop()

    f = open('colisoes.txt', 'w')
    for item in colisoes_feito:
        f.write(item)
    f.close()
    return


map_maker()
