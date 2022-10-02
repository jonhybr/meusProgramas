import pygame
from pygame.locals import *
from pygame.math import Vector2
import math

pygame.init()
Display_Size = (500, 500)
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

sprites = {'pistola': pygame.transform.scale2x(pygame.image.load("pistola.png")), 'fogo': pygame.transform.scale2x(pygame.image.load("fogo.png")),
           'gelo': pygame.transform.scale2x(pygame.image.load("gelo.png")), 'bola_de_fogo': pygame.image.load("bola_fogo.png"), 'bala': pygame.image.load("bala.png"),
           'estaca_gelo': pygame.image.load("estaca_gelo.png"), 'borda': pygame.transform.scale2x(pygame.image.load('borda.png')), 'borda_a': pygame.transform.scale2x(pygame.image.load("borda_a.png")),
           'personagem_pistola': pygame.transform.scale2x(pygame.image.load('personagem_pistola.png')), 'personagem_varinha': pygame.transform.scale2x(pygame.image.load('personagem_varinha.png')),
           'personagem_treino': pygame.transform.scale2x(pygame.image.load('personagem_treino.png'))}

personagem = sprites['personagem_pistola']
personagem_pos = personagem.get_rect()
personagem_pos.center = (Display_Size[0] // 2, Display_Size[1] // 2)

inventario = [sprites['pistola'], sprites['gelo'], sprites['fogo']]

speed = 2
move = [0, 0]

bala = sprites['bala']
bala_pos = sprites['bala'].get_rect()
bullet_speed = 5

tiros = []
remover_ba = []
remover_bl = []
blocos = []

selecionado = 'p'

while True:
    Display.fill((180, 180, 180))

    mouse = pygame.mouse.get_pos()

    personagem_pos[0] += move[0]
    personagem_pos[1] += move[1]

    px = mouse[0] - personagem_pos.center[0]
    py = mouse[1] - personagem_pos.center[1]
    if px == 0:
        px = 0.1
    if py == 0:
        py = 0.1
    theta = math.atan(px / py)
    theta = math.degrees(theta)

    if personagem_pos.left < 0:
        personagem_pos.left = 0
    if personagem_pos.right > Display_Size[0]:
        personagem_pos.right = Display_Size[0]

    if personagem_pos.top < 0:
        personagem_pos.top = 0
    if personagem_pos.bottom > Display_Size[1]:
        personagem_pos.bottom = Display_Size[1]

    print(personagem_pos)

    if py > 0:
        theta += 180

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == BUTTON_LEFT:
                tiros.append([personagem_pos.center[0], personagem_pos.center[1], theta, 100, bala])
            if event.button == BUTTON_RIGHT:
                blocos.append([mouse[0], mouse[1], theta])
        if event.type == KEYDOWN:
            if event.key == K_1:
                selecionado = 'p'
                bala = sprites['bala']
                personagem = sprites['personagem_pistola']
            if event.key == K_2:
                selecionado = 'g'
                bala = sprites['estaca_gelo']
                personagem = sprites['personagem_varinha']
            if event.key == K_3:
                selecionado = 'f'
                bala = sprites['bola_de_fogo']
                personagem = sprites['personagem_varinha']
            if event.key == K_d:
                move[0] = speed
            if event.key == K_a:
                move[0] = -speed
            if event.key == K_s:
                move[1] = speed
            if event.key == K_w:
                move[1] = -speed
        if event.type == KEYUP:
            if event.key == K_d and move[0] == speed or event.key == K_a and move[0] == -speed:
                move[0] = 0
            if event.key == K_s and move[1] == speed or event.key == K_w and move[1] == -speed:
                move[1] = 0

    for bloco in blocos:
        Display.blit(pygame.transform.rotate(sprites['personagem_treino'], (bloco[2] - 180)), (bloco[0], bloco[1]))

    c = 0
    for tiro in tiros:
        tiro[0] += bullet_speed * math.sin((tiro[2] + 180) * math.pi / 180)
        tiro[1] += bullet_speed * math.cos((tiro[2] + 180) * math.pi / 180)
        bala_pos[0] = tiro[0]
        bala_pos[1] = tiro[1]
        Display.blit(pygame.transform.rotate(tiro[4], tiro[2]), (tiro[0], tiro[1]))
        b = 0
        for block in blocos:
            bloco = pygame.Surface((20, 20))
            bloco_pos = bloco.get_rect()
            bloco_pos[0] = block[0]
            bloco_pos[1] = block[1]
            if bala_pos.colliderect(bloco_pos):
                remover_bl.append(b)
                remover_ba.append(c)
            b += 1
        tiro[3] -= 1
        if tiro[3] == 0:
            remover_ba.append(c)
        c += 1

    x = 20
    y = Display_Size[1] - 60
    for slot in range(0, 3):
        if selecionado == 'p' and slot == 0:
            Display.blit(sprites['borda_a'], (x, y))
        elif selecionado == 'g' and slot == 1:
            Display.blit(sprites['borda_a'], (x, y))
        elif selecionado == 'f' and slot == 2:
            Display.blit(sprites['borda_a'], (x, y))
        else:
            Display.blit(sprites['borda'], (x, y))
        if len(inventario) > slot:
            Display.blit(inventario[slot], (x + 4, y + 4))
        x += 40

    for fim in remover_ba:
        tiros.pop(fim)
        remover_ba.pop(0)

    for fim in remover_bl:
        blocos.pop(fim)
        remover_bl.pop(0)

    Display.blit(pygame.transform.rotate(personagem, theta), personagem_pos)

    Clock.tick(60)
    pygame.display.update()
