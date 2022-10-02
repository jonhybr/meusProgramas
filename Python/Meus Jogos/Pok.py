import pygame
from pygame.locals import *

pygame.init()
Display_Width = 500
Display_Height = 400
Display = pygame.display.set_mode((Display_Width, Display_Height))
Clock = pygame.time.Clock()


monstros = [{'Nome': 'Aranha', 'Dano':5, 'Vida': 100}]


def terminate():
    pygame.quit()
    quit()


def check_exit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


def escrever(tpos=(), tam=30, texto='', qualidade=True, cor=(0, 0, 0)):
    fonte = pygame.font.SysFont(None, tam)
    texto = fonte.render(texto, qualidade, cor, None)
    return Display.blit(texto, tpos)


def main():
    while True:
        game_loop()
        batalha()


def game_loop():
    pos = [32, 32]
    tamanho = (32, 32)
    p1 = pygame.Surface(tamanho)
    p1.fill((100, 100, 100))

    posI = [128, 128]
    inimigo = pygame.Surface(tamanho)
    inimigo.fill((200, 50, 50))
    while True:
        check_exit()

        if posI[1] - 32 == pos[1] and posI[0] == pos[0] or posI[0] - 32 == pos[0] and posI[1] == pos[1] \
                or pos[0] - 32 == posI[0] and pos[1] == posI[1] or pos[1] - 32 == posI[1] and pos[0] == posI[0]:
            batalha(monstros[0]['Nome'], monstros[0]['Dano'], monstros[0]['Vida'])

        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    pos[0] += 32
                if pos[0] != 0:
                    if event.key == K_LEFT:
                        pos[0] -= 32
                if event.key == K_DOWN:
                    pos[1] += 32
                if pos[1] != 0:
                    if event.key == K_UP:
                        pos[1] -= 32

        Display.fill((0, 0, 0))

        Display.blit(inimigo, posI)
        Display.blit(p1, pos)

        pygame.display.update()
        Clock.tick(60)


def combate(pos):
    mousepos = pygame.mouse.get_pos()
    for loc in range(0, len(pos)):
        if pos[loc][0] < mousepos[0] < pos[loc][0] + 60 and pos[loc][1] < mousepos[1] < pos[loc][1] + 30:
            return loc


def batalha(inimigo='Unknow', dano=5, vidaini=20):
    opcoes = ['Lutar', 'Trocar', 'Item', 'Fugir']
    op = []
    tam = 150
    vidaatual = vidaini
    vida = pygame.Surface((12, 12))
    vida.fill((0, 160, 0))
    ivp = [30, 30]
    jvp = [310, 250]
    while True:
        check_exit()

        Display.fill((255, 255, 255))

        if tam <= 0:
            return game_loop()

        barraini = pygame.Surface((tam, 10))
        barrajog = pygame.Surface((150, 10))

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                opc = combate(op)
                if opc is not None:
                    if opc == 0:
                        vidaatual -= 5
                        tam = vidaatual * (150 / vidaini)
                    if opc == 3:
                        game_loop()

        y = 300
        x = 300
        for linha in range(0, len(opcoes)):
            if linha == 2:
                x = 300
                y += 50
            escrever((x, y), 30, opcoes[linha], cor=(100, 100, 100))
            if [x, y] not in op:
                op.append([x, y])
            x += 100

        escrever((310, 230), 20, 'Jogador', True, (100, 100, 100))
        escrever((30, 10), 20, inimigo, True, (100, 100, 100))
        Display.blit(barraini, ivp)
        Display.blit(barrajog, jvp)
        pygame.display.update()
        Clock.tick(60)


if __name__ == '__main__':
    main()
