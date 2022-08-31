import pygame
from pygame.locals import *
from random import randint
from commons import *

pygame.init()
Display_Size = [500, 400]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

chao = desenhar((Display_Size[0], 50), (150, 80, 30))
grama = desenhar((Display_Size[0], 10), (80, 150, 80))

jogador = desenhar((16, 32))
jogador_col = jogador.get_rect()
jogador_col.center = (Display_Size[0] // 2, 324)
move = 0

cores = [(100, 255, 100), (255, 100, 100), (220, 220, 100)]
fruta = desenhar((20, 20))
fx = fy = 0
frutas = []
gerar = False
time = 30
passaram = []

maças = limoes = abacaxis = 0

while True:
    check_exit()
    Display.fill((200, 200, 220))

    jogador_col.x += move

    if time >= 30:
        gerar = True
        time = 0

    time += 1

    if gerar:
        quantidade = randint(2, 6)
        for q in range(0, quantidade):
            fx = randint(0, Display_Size[0] - 20)
            fy = -50 + randint(-30, 30)
            cor = randint(0, 2)
            frutas.append({'Pos': [fx, fy], 'Cor': cores[cor]})
        gerar = False

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move = 5
            if event.key == K_LEFT:
                move = -5
        if event.type == KEYUP:
            if event.key == K_RIGHT and move == 5 or event.key == K_LEFT and move == -5:
                move = 0

    if jogador_col.right > Display_Size[0]:
        jogador_col.right = Display_Size[0]
    if jogador_col.left < 0:
        jogador_col.left = 0

    for f in frutas:
        fruta.fill(f['Cor'])
        Display.blit(fruta, f['Pos'])
        f['Pos'][1] += 3
        if f['Pos'][0] + 20 > jogador_col.left and f['Pos'][0] < jogador_col.right and f['Pos'][1] + 20 > jogador_col.top and f['Pos'][1] < jogador_col.bottom:
            passaram.append(f.copy())
            if f['Cor'] == (255, 100, 100):
                maças += 1
            if f['Cor'] == (100, 255, 100):
                limoes += 1
            if f['Cor'] == (220, 220, 100):
                abacaxis += 1
        if f['Pos'][1] > 340:
            passaram.append(f.copy())

    for pas in passaram:
        frutas.remove(pas)
    passaram.clear()

    pontos = escreve(f'Maçãs: {maças} | Limões: {limoes} | Abacaxis: {abacaxis}', 20, (250, 250, 250), antialias=True)
    Display.blit(pontos[0], (5, 5))
    Display.blit(jogador, jogador_col)
    Display.blit(grama, (0, 340))
    Display.blit(chao, (0, 350))
    pygame.display.update()
    Clock.tick(60)

