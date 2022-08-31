import pygame
from pygame.locals import *

pygame.init()

Display_Width = 500
Display_Height = 550
Display = pygame.display.set_mode((Display_Width, Display_Height))
Clock = pygame.time.Clock()

tamanho = 32

nave = pygame.image.load('nave.png')
pos = [Display_Width // 2, Display_Height - 80]
movimento = 0

tiro = pygame.Surface((10, 10))
tiro.fill((255, 255, 255))
tiros = []
delay = 15

invasor = pygame.image.load('alien1.png')
posA = []
moveA = 1
moveAX = 0
moveAY = 0
saiu = False

y = 0
for camada in range(0, 6):
    x = 0
    for position in range(0, 10):
        posA.append([x + 40 + moveAX, y + 30 + moveAY])
        x += tamanho + 10
    y += tamanho + 10

colid = []

atirando = False

while True:

    if delay < 10:
        delay += 1
    else:
        if atirando:
            tiros.append([pos[0] + tamanho // 2, pos[1]])
            delay = 0

    if len(posA) < 1:
        break

    pos[0] += movimento

    if pos[0] + tamanho > Display_Width:
        pos[0] = Display_Width - tamanho
    if pos[0] < 0:
        pos[0] = 0

    Display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                movimento = 5
            if event.key == K_LEFT:
                movimento = -5
            if event.key == K_UP:
                atirando = True

        if event.type == KEYUP:
            if event.key == K_RIGHT and movimento == 5 or event.key == K_LEFT and movimento == -5:
                movimento = 0
            if event.key == K_UP:
                atirando = False

    for local in range(0, len(posA)):
        Display.blit(pygame.transform.scale(invasor, (tamanho, tamanho)), (posA[local][0], posA[local][1]))
        posA[local][0] += moveA
        if posA[local][0] < 0 or posA[local][0] + tamanho > Display_Width:
            saiu = True
        if posA[local][0] == posA[-1][0] and saiu:
            moveA *= -1
            for queda in range(0, len(posA)):
                posA[queda][1] += 10
            saiu = False

    if len(tiros) > 0:
        for t in range(0, len(tiros)):
            Display.blit(tiro, (tiros[t][0], tiros[t][1]))
            tiros[t][1] -= 6

    for passou in range(0, len(tiros)):
        if tiros[passou][1] < -10:
            tiros.pop(passou)
            break

    for disparos in range(0, len(tiros)):
        for acertou in range(0, len(posA)):
            if posA[acertou][1] + tamanho > tiros[disparos][1] and posA[acertou][1] < tiros[disparos][1] + 10:
                if posA[acertou][0] < tiros[disparos][0] + 10 and posA[acertou][0] + tamanho > tiros[disparos][0]:
                    colid.append([disparos, acertou])
                    break

    if len(colid) > 0:
        posA.pop(colid[0][1])
        tiros.pop(colid[0][0])
        colid.clear()

    Display.blit(pygame.transform.scale(nave, (tamanho, tamanho)), pos)
    pygame.display.update()
    Clock.tick(30)
