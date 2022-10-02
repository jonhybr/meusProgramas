import pygame, sys
from pygame.locals import *

pygame.init()

Display_Width = 600
Display_Height = 400
Display = pygame.display.set_mode((Display_Width, Display_Height))
Clock = pygame.time.Clock()
linha = pygame.Surface((4, 20))
linha.fill((255, 255, 255))
op = 0
pontos = [0, 0]


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYDOWN):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


def main():
    global op
    start_Screen()
    while True:
        game_loop()
        end_game()


def start_Screen():
    global op, pontos

    pontos = [0, 0]

    pygame.event.clear()

    font = pygame.font.SysFont('calibri', 50)
    font2 = pygame.font.SysFont('calibri', 30)
    texto = font.render('Pingo Pongo!', True, (255, 255, 255))
    texto2 = font2.render('JvsJ', True, (255, 255, 255), (120, 120, 120))
    texto3 = font2.render('JvsBot', True, (255, 255, 255), (120, 120, 120))
    centro = texto.get_rect()
    centro2 = texto2.get_rect()
    centro3 = texto3.get_rect()
    centro.center = (Display_Width // 2, Display_Height // 2 - 50)
    centro2.center = (150, Display_Height - 100)
    centro3.center = (Display_Width - 150, Display_Height - 100)
    while True:

        checkForQuit()

        mousePos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if centro2[0] < mousePos[0] < centro2[0] + centro2[2]:
                if centro2[1] < mousePos[1] < centro2[1] + centro2[3]:
                    if event.type == MOUSEBUTTONUP:
                        op = 1
                        return
            if centro3[0] < mousePos[0] < centro3[0] + centro3[2]:
                if centro3[1] < mousePos[1] < centro3[1] + centro3[3]:
                    if event.type == MOUSEBUTTONUP:
                        op = 2
                        return

        Display.fill((0, 0, 0))

        Display.blit(texto, centro)
        Display.blit(texto2, centro2)
        Display.blit(texto3, centro3)

        pygame.display.update()
        Clock.tick(30)


def game_loop():
    global op, pontos
    pygame.event.clear()

    corBola = (255, 255, 255)

    tamanhox = 10
    tamanhoy = 80

    jogador1 = pygame.Surface((tamanhox, tamanhoy))
    jogador1.fill((255, 255, 255))

    jogador2 = pygame.Surface((tamanhox, tamanhoy))
    jogador2.fill((255, 255, 255))

    px1 = 5
    py1 = Display_Height // 2 - tamanhoy // 2
    px2 = Display_Width - tamanhox - 5
    py2 = Display_Height // 2 - tamanhoy // 2

    movimentoy1 = 0
    movimentoy2 = 0
    velocidade = 6

    tamanhoB = 10

    movimentoBolax = -10
    movimentoBolay = 0
    velocidadeB = 10

    bolax = Display_Width // 2
    bolay = Display_Height // 2

    while True:
        checkForQuit()

        py1 += movimentoy1
        py2 += movimentoy2
        bolax += movimentoBolax
        bolay += movimentoBolay

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w:
                    movimentoy1 = -velocidade
                if event.key == K_s:
                    movimentoy1 = velocidade
                if op == 1:
                    if event.key == K_UP:
                        movimentoy2 = -velocidade
                    if event.key == K_DOWN:
                        movimentoy2 = velocidade

            if event.type == KEYUP:
                if event.key == K_w and movimentoy1 == -velocidade or \
                        event.key == K_s and movimentoy1 == velocidade:
                    movimentoy1 = 0
                if event.key == K_UP and movimentoy2 == -velocidade or \
                        event.key == K_DOWN and movimentoy2 == velocidade:
                    movimentoy2 = 0

        if op == 2:
            if bolax > 200:
                if bolay < py2 + tamanhoy // 2 - 15:
                    movimentoy2 = -velocidade
                if bolay > py2 + tamanhoy // 2 + 15:
                    movimentoy2 = velocidade
            else:
                movimentoy2 = 0

        if bolax - tamanhoB < px1 + tamanhox or bolax + tamanhoB > px2:
            if bolax < Display_Width // 2:
                if bolay - tamanhoB < py1 + tamanhoy and bolay + tamanhoB > py1:
                    if movimentoy1 == velocidade:
                        movimentoBolax = velocidadeB + 2
                        movimentoBolay = 6
                        corBola = (255, 200, 200)
                    elif movimentoy1 == -velocidade:
                        movimentoBolax = velocidadeB + 2
                        movimentoBolay = -6
                        corBola = (255, 200, 200)
                    else:
                        corBola = (255, 255, 255)
                        movimentoBolax = velocidadeB
                        if movimentoBolay > 0:
                            movimentoBolay = 5
                        elif movimentoBolay < 0:
                            movimentoBolay = -5

            if bolax > Display_Width // 2:
                if bolay - tamanhoB < py2 + tamanhoy and bolay + tamanhoB > py2:
                    if movimentoy2 < 0:
                        movimentoBolax = -velocidadeB - 2
                        movimentoBolay = -6
                        corBola = (255, 200, 200)
                    elif movimentoy2 > 0:
                        movimentoBolax = -velocidadeB - 2
                        movimentoBolay = 6
                        corBola = (255, 200, 200)
                    else:
                        corBola = (255, 255, 255)
                        movimentoBolax = -velocidadeB
                        if movimentoBolay > 0:
                            movimentoBolay = 5
                        elif movimentoBolay < 0:
                            movimentoBolay = -5

        if bolax < 0:
            pontos[1] += 1
            game_loop()
        if bolax > Display_Width:
            pontos[0] += 1
            game_loop()
        if pontos[0] == 5 or pontos[1] == 5:
            return

        if bolay + tamanhoB > Display_Height or bolay - tamanhoB < 0:
            movimentoBolay *= -1

        if py1 < 0:
            py1 = 0
        if py1 + tamanhoy > Display_Height:
            py1 = Display_Height - tamanhoy
        if py2 < 0:
            py2 = 0
        if py2 + tamanhoy > Display_Height:
            py2 = Display_Height - tamanhoy

        Display.fill((0, 0, 0))

        py = -2
        for c in range(0, 14):
            px = Display_Width // 2 - 2
            Display.blit(linha, (px, py))
            py += 35

        Display.blit(jogador1, (px1, py1))
        Display.blit(jogador2, (px2, py2))

        Display.blit(pygame.font.SysFont('calibri', 30).render(f'{pontos[0]}', True, (255, 255, 255)),
                     (Display_Width // 2 // 2, 20))
        Display.blit(pygame.font.SysFont('calibri', 30).render(f'{pontos[1]}', True, (255, 255, 255)),
                     (Display_Width // 2 + Display_Width // 4, 20))

        pygame.draw.circle(Display, corBola, (bolax, bolay), tamanhoB, 0)

        pygame.display.update()

        Clock.tick(60)


def end_game():
    font = pygame.font.SysFont('ok', 50)
    texto1 = font.render('O jogador 1 Ganhou!' if pontos[0] == 5 else 'O jogador 2 Ganhou!', True, (255, 255, 255))
    texto2 = font.render('O jogador Ganhou!' if pontos[0] == 5 else 'O Bot Ganhou!', True, (255, 255, 255))
    centro = texto1.get_rect()
    centro2 = texto2.get_rect()
    centro.center = (Display_Width // 2, Display_Height // 2)
    centro2.center = (Display_Width // 2, Display_Height // 2)
    while True:
        checkForQuit()

        for event in pygame.event.get(MOUSEBUTTONUP):
            main()

        Display.fill((0, 0, 0))

        if op == 1:
            Display.blit(texto1, centro)
        else:
            Display.blit(texto2, centro2)

        pygame.display.update()


if __name__ == '__main__':
    main()
