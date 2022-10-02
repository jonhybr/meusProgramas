import pygame
from pygame.locals import *


pygame.init()
Display_Size = [512, 384]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

f = open('texto' + '.txt', 'r')
read = f.read()
f.close()
read = read.split('\n')
mapa = []
for linha in read:
    mapa.append(list(linha))

jogador = pygame.image.load('personagem.png').convert_alpha()
jogador_scale = pygame.transform.scale(jogador, (23, 32))
jogador_pos = jogador_scale.get_rect()
jogador_pos.x = 200
jogador_pos.y = 200

faca = pygame.image.load('faca.png')
faca_pos = faca.get_rect()

move = [0, 0]
spd = 3
moving_right = True
gravidade = 0

craby = pygame.image.load('carangueijo.png')
craby_pos = craby.get_rect()
inimigos_dict = {'nome': 'carangueijo', 'image': craby, 'pos': craby_pos}
inimigos = []

grama = pygame.image.load('images/grama.png').convert()
grama_d = pygame.image.load('images/grama_d.png').convert()
grama_e = pygame.image.load('images/grama_e.png').convert()
terra = pygame.image.load('images/terra.png').convert()

colisiveis = []

pulo = False

scroll = [0, 0]

move_scroll = 0

while True:

    Display.fill((200, 200, 255))
    if moving_right:
        Display.blit(jogador_scale, (jogador_pos[0] - scroll[0], jogador_pos[1] - scroll[1]))
        Display.blit(faca, (faca_pos.x - 2 + jogador_pos.x + jogador_pos.width - scroll[0], faca_pos.y + jogador_pos.y + 10 - scroll[1]))
    else:
        Display.blit(pygame.transform.flip(jogador_scale, 180, 0), (jogador_pos[0] - scroll[0], jogador_pos[1] - scroll[1]))
        Display.blit(pygame.transform.flip(faca, 180, 0), (faca_pos.x + 2 + jogador_pos.x - faca_pos.width - scroll[0], faca_pos.y + jogador_pos.y + 10 - scroll[1]))

    scroll[0] += (jogador_pos.x - scroll[0] - 221)
    if scroll[0] < 0:
        scroll[0] = 0
    scroll[1] += (jogador_pos.y - scroll[1] - 244)
    if scroll[1] > 30:
        scroll[1] = 30

    if jogador_pos[1] > Display_Size[1]:
        jogador_pos.x = 200
        jogador_pos.y = 200

    if gravidade < 5:
        gravidade += 0.2

    colisiveis = []
    inimigos = []
    y = 0
    for linha in mapa:
        x = 0
        for pos in linha:
            if pos == '2':
                Display.blit(grama, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if pos == '1':
                Display.blit(grama_e, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if pos == '3':
                Display.blit(grama_d, (x * 32 - scroll[0], y * 32 - scroll[1]))
            if pos == '4':
                Display.blit(terra, (x * 32 - scroll[0], y * 32 - scroll[1]))
                #inimigos_dict['pos'] = x * 32 - scroll[0], y * 32 - scroll[1], 32, 32
                #Display.blit(inimigos_dict['image'], inimigos_dict['pos'])
                #inimigos.append(pygame.Rect(inimigos_dict['pos']))
            if pos != '0':
                colisiveis.append(pygame.Rect(x * 32, y * 32, 32, 32))
            x += 1
        y += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        if event.type == KEYUP:
            if event.key == K_RIGHT and move[0] == spd or event.key == K_LEFT and move[0] == -spd:
                move[0] = 0
            if event.key == K_DOWN and move[1] == spd or event.key == K_UP and move[1] == -spd:
                move[1] = 0

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move[0] = spd
                moving_right = True
            if event.key == K_LEFT:
                moving_right = False
                move[0] = -spd
            if pulo:
                if event.key == K_UP:
                    gravidade = -6
                    pulo = False

    for inimigo in inimigos:
        inimigo[0] += 2
        if jogador_pos.colliderect(inimigo):
            break

    jogador_pos.x += move[0]
    for colisao in colisiveis:
        if jogador_pos.colliderect(colisao):
            if move[0] > 0:
                jogador_pos.right = colisao.left
            if move[0] < 0:
                jogador_pos.left = colisao.right

    jogador_pos.y += move[1] + gravidade
    for colisao in colisiveis:
        if jogador_pos.colliderect(colisao):
            if gravidade > 0:
                jogador_pos.bottom = colisao.top
                gravidade = 1
                pulo = True
            if gravidade < 0:
                jogador_pos.top = colisao.bottom
                gravidade = 0

    pygame.display.update()
    dt = Clock.tick(60)
