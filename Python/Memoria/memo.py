import pygame
from pygame.locals import *
from commons import *
from random import randint

pygame.init()

Display_Size = [500, 500]
Display = pygame.display.set_mode(Display_Size)

Clock = pygame.time.Clock()


def main():
    tela_inicial()
    while True:
        print('a')
        #game_loop()
        #end_game()


def tela_inicial():
    titulo = escreve('Jogo Da Memória', 50, (255, 255, 255), True)
    titulo[1].center = (Display_Size[0] // 2, Display_Size[1] // 2 - 80)
    opcoes = ['5x4', '6x5', '7x6']
    opcoes_col = []
    while True:
        Display.fill((80, 80, 80))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                for op in opcoes_col:
                    if op[0] < mouse[0] < op[0] + op[2] and op[1] < mouse[1] < op[1] + op[3]:
                        if op == opcoes_col[0]:
                            game_loop(5, 4)
                        if op == opcoes_col[1]:
                            game_loop(6, 5)
                        if op == opcoes_col[2]:
                            game_loop(7, 6)
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                pygame.event.post(event)

        Display.blit(titulo[0], titulo[1])
        x = 150
        y = 250
        for op in opcoes:
            op_es = escreve(op, 30, (255, 255, 255), True)
            op_es[1].center = (x, y)
            contorno = pygame.Surface((70, 30))
            contorno_centro = contorno.get_rect()
            contorno_centro.center = (x, y)
            if contorno_centro not in opcoes_col:
                opcoes_col.append(contorno_centro)
            Display.blit(contorno, contorno_centro)
            Display.blit(op_es[0], op_es[1])
            x += 100

        Clock.tick(30)
        pygame.display.update()


def game_loop(linhas, colunas):
    game_area = linhas * colunas
    cartas = []
    for carta in range(0, game_area // 2):
        cartas.append(carta + 1)
        cartas.append(carta + 1)

    padrao = []
    gerado = []
    for carta in range(0, game_area):
        lugar = randint(0, game_area - 1)
        while lugar in gerado:
            lugar = randint(0, game_area - 1)
        gerado.append(lugar)
        padrao.append(cartas[lugar])

    espaco = 20
    carta_tam = [32, 50]
    remover = []
    selecionado = []
    while True:
        Display.fill((255, 255, 255))

        x = ((Display_Size[0] - (linhas * (carta_tam[0] + espaco) - espaco)) // 2)
        y = ((Display_Size[1] - (colunas * (carta_tam[1] + espaco) - espaco)) // 2)
        cartas_col = []
        carta = 0
        for linha in range(0, colunas):
            for pos in range(0, linhas):
                if (pygame.Rect(x, y, carta_tam[0], carta_tam[1])) not in remover:
                    cartas_col.append(pygame.Rect(x, y, carta_tam[0], carta_tam[1]))
                    Display.blit(pygame.Surface(carta_tam), (x, y))
                    simbolo = escreve(str(padrao[carta]), 20, (100, 100, 100), True)
                    simbolo[1].center = (x + carta_tam[0] // 2, y + carta_tam[1] // 2)
                    Display.blit(simbolo[0], simbolo[1])
                carta += 1
                x += espaco + carta_tam[0]
            x = ((Display_Size[0] - (linhas * (carta_tam[0] + espaco) - espaco)) // 2)
            y += carta_tam[1] + espaco

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                mouse_col = pygame.Rect(mouse[0], mouse[1], 1, 1)
                count = 0
                for col in cartas_col:
                    if mouse_col.colliderect(col):
                        print(padrao[count])
                        remover.append(col)

                    count += 1


        pygame.display.update()
        Clock.tick(60)


main()


