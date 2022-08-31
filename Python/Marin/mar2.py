import pygame
from pygame.locals import *

pygame.init()
Display_Size = [800, 400]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

f = open('mapa' + '.txt', 'r')
read = f.read()
f.close()
read = read.split('\n')
mapa = []
sprite = ''
for linha in read:
    camada = []
    for pos in linha:
        if pos != ',':
            sprite += pos
        else:
            camada.append(sprite)
            sprite = ''
    mapa.append(camada)


def img_load(sprite):
    img = pygame.image.load('sprites/' + sprite).convert()
    img = pygame.transform.scale2x(img)
    return img


sprites = {'grama': img_load('grama.png'), 'grama_ce': img_load('grama_ce.png'), 'grama_cd': img_load('grama_cd.png'),
           'grama_be': img_load('grama_be.png'), 'grama_bd': img_load('grama_bd.png'),
           'grama_e': img_load('grama_e.png'),
           'grama_d': img_load('grama_d.png'), 'grama_b': img_load('grama_b.png'), 'terra': img_load('terra.png'),
           'pedra': img_load('pedra.png'), 'tijolo': img_load('tijolo.png'), 'player': pygame.transform.scale2x(pygame.image.load('sprites/player.png')),
           'player1': pygame.transform.scale2x(pygame.image.load('sprites/player_and1.png')), 'player2': pygame.transform.scale2x(pygame.image.load('sprites/player_and2.png'))}


def main_game():
    player = [100, 100, sprites['player']]
    move = [0, 0]
    max_speed = 5
    move_speed = 0.2
    moving = {'right': False, 'left': False, 'up': False, 'down': False}
    c = 0
    while True:
        Display.fill((240, 240, 240))

        y = Display_Size[1] - (len(read) * 32)
        for camada in mapa:
            x = 0
            for spr in camada:
                if spr != '0':
                    Display.blit(sprites[spr], (x, y))
                x += 32
            y += 32

        player[0] += move[0]
        player[1] += move[1]

        if moving['right']:
            if move[0] < max_speed:
                move[0] += move_speed
        if moving['left']:
            if move[0] > -max_speed:
                move[0] -= move_speed
        if moving['down']:
            if move[1] < max_speed:
                move[1] += move_speed
        if moving['up']:
            if move[1] > -max_speed:
                move[1] -= move_speed

        if move != [0, 0]:
            if player[2] == sprites['player'] and c == 7:
                player[2] = sprites['player1']
                c = 0
            if player[2] == sprites['player1'] and c == 7:
                player[2] = sprites['player2']
                c = 0
            if player[2] == sprites['player2'] and c == 7:
                player[2] = sprites['player1']
                c = 0
            c += 1
        else:
            player[2] = sprites['player']

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == K_RIGHT:
                    moving['right'] = True
                if event.key == K_LEFT:
                    moving['left'] = True
                if event.key == K_UP:
                    moving['up'] = True
                if event.key == K_DOWN:
                    moving['down'] = True

            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving['right'] = False
                    move[0] = 0
                if event.key == K_LEFT:
                    moving['left'] = False
                    move[0] = 0
                if event.key == K_UP:
                    moving['up'] = False
                    move[1] = 0
                if event.key == K_DOWN:
                    moving['down'] = False
                    move[1] = 0

        Display.blit(player[2], (player[0], player[1]))
        Clock.tick(60)
        pygame.display.update()


main_game()
