import pygame
from pygame.locals import *
from random import randint

pygame.init()
Display_Width = 400
Display_Height = 400
Display = pygame.display.set_mode((Display_Width, Display_Height))
Clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYDOWN):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


def main():
    start_screen()
    while True:
        game_loop()
        end_game()


def start_screen():
    font = pygame.font.SysFont('ola', 70)
    font2 = pygame.font.SysFont('ola', 40)
    texto = font.render('Pongo Game', True, (255, 255, 255))
    texto2 = font2.render('Start', True, (100, 200, 100))
    centro = texto.get_rect()
    centro.center = (Display_Width // 2, Display_Height // 3)
    centro2 = texto2.get_rect()
    centro2.center = (Display_Width // 2, Display_Height // 2)

    while True:
        mousePos = pygame.mouse.get_pos()
        checkForQuit()
        Display.fill((0, 0, 0))

        for event in pygame.event.get(MOUSEBUTTONUP):
            if mousePos[0] > centro2[0] and mousePos[0] < centro2[0] + centro2[2]:
                if mousePos[1] > centro2[1] and mousePos[1] < centro2[1] + centro2[3]:
                    return

        Display.blit(texto, centro)
        Display.blit(texto2, centro2)
        pygame.display.update()
        Clock.tick(60)


def game_loop():
    player = pygame.Surface((80, 10))
    player.fill((255, 255, 255))
    posp = player.get_rect()
    posp.center = (Display_Width // 2, Display_Height - 50)
    movimentop = 0

    bolax = Display_Width // 2
    bolay = Display_Height - 100
    tamanhob = 8
    movimentov = 5
    movimentob = 0

    cores = [[205, 0, 0], [0, 205, 0], [0, 0, 205], [205, 205, 0], [0, 205, 205], [205, 0, 205]]
    cor = []
    apr = []
    for c in range(0, 6):
        random = randint(0, len(cores) - 1)
        while random in apr:
            random = randint(0, len(cores) - 1)
        apr.append(random)
        cor.append(cores[random])

    barra = pygame.Surface((40, 20))
    barras = []
    y = 0
    for camada in range(0, 6):
        barra.fill(cor[y])
        x = 0
        for pos in range(0, 7):
            barras.append([x * 50 + 30, y * 30 + 10])
            x += 1
        y += 1

    while True:
        checkForQuit()

        posp[0] += movimentop
        bolax += movimentob
        bolay += movimentov

        if posp[0] < 0:
            posp[0] = 0
        if posp[0] + posp[2] > Display_Width:
            posp[0] = Display_Width - posp[2]

        if bolay + tamanhob > posp[1] and bolay - tamanhob < posp[1] + 10\
                and bolax + tamanhob > posp[0] and bolax - tamanhob < posp[0] + 80:
            if movimentob == 0:
                if movimentop == 5:
                    movimentob = 2
                elif movimentop == -5:
                    movimentob = -2
            movimentov = -5

        if bolay - tamanhob < 0:
            movimentov = 5
        if bolay + tamanhob > Display_Height:
            game_loop()
        if bolax - tamanhob < 0 or bolax + tamanhob > Display_Width:
            movimentob *= -1

        for col in range(0, len(barras)):
            if barras[col][0] + 2 > bolax > barras[col][0] - 5 and barras[col][1] - 1 < bolay < barras[col][1] + 21:
                movimentob *= -1
                barras[col] = [0, 0]

            if barras[col][0] + 38 < bolax < barras[col][0] + 45 and barras[col][1] - 1 < bolay < barras[col][1] + 21:
                movimentob *= -1
                barras[col] = [0, 0]

            if barras[col][0] < bolax < barras[col][0] + 40 and barras[col][1] + 25 > bolay - tamanhob < barras[col][1] + 18:
                movimentov *= -1
                barras[col] = [0, 0]

            if barras[col][0] < bolax < barras[col][0] + 40 and barras[col][1] + 2 > bolay + tamanhob < barras[col][1] - 5:
                movimentov *= -1
                barras[col] = [0, 0]

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    movimentop = 5
                if event.key == K_LEFT:
                    movimentop = -5
            if event.type == KEYUP:
                if event.key == K_RIGHT and movimentop == 5 or event.key == K_LEFT and movimentop == -5:
                    movimentop = 0

        Display.fill((0, 0, 0))

        count = 0
        barra.fill(cor[0])
        for pos in range(0, len(barras)):
            if barras[pos][0] != 0:
                if pos > 6:
                    barra.fill(cor[1])
                if pos > 13:
                    barra.fill(cor[2])
                if pos > 20:
                    barra.fill(cor[3])
                if pos > 27:
                    barra.fill(cor[4])
                if pos > 34:
                    barra.fill(cor[5])
                Display.blit(barra, barras[pos])
            if barras[pos][0] == 0:
                count += 1
                if count == 42:
                    main()

        pygame.draw.circle(Display, (255, 255, 255), (bolax, bolay), tamanhob)

        Display.blit(player, posp)

        pygame.display.update()
        Clock.tick(60)


def end_game():
    while True:

        checkForQuit()
        Display.fill((0, 0, 0))
        pygame.display.update()
        Clock.tick(60)


if __name__ == '__main__':
    main()