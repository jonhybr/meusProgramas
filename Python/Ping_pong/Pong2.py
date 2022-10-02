import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Arkanoid')
Display_Size = [500, 550]
Display = pygame.display.set_mode(Display_Size)
game_Display_Size = [Display_Size[0] - 40, Display_Size[1] - 80]
game_Display = pygame.Surface(game_Display_Size)

bg = pygame.image.load('sprites/bg.png')

try:
    f = open('highscore.txt', 'r')
    hs = int(f.read())

except ValueError:
    f = open('highscore.txt', 'w')
    f.write(str(0))
    hs = 0

except FileNotFoundError:
    f = open('highscore.txt', 'w')
    hs = 0

f.close()

Clock = pygame.time.Clock()

barra_qtd = 10
bola_spd = 5
spd = 5

vidas = 5

pontos = 0

cores = {'vermelho': pygame.image.load('sprites/barra_v.png'),
         'amarelo': pygame.image.load('sprites/barra_a.png'),
         'azul': pygame.image.load('sprites/barra_az.png'),
         'roxo': pygame.image.load('sprites/barra_r.png'),
         'verde': pygame.image.load('sprites/barra_verd.png')}


def escreve(texto, tam=32, cor=(0, 0, 0), antialias=False):
    font = pygame.font.SysFont('calibri', tam)
    text = font.render(texto, antialias, cor)
    pos = text.get_rect()
    return text, pos


def game_loop():
    global hs, barra_qtd, spd, vidas, pontos

    remover = []

    jogador = pygame.image.load('sprites/barra.png')
    jogador_pos = jogador.get_rect()
    jogador_pos.center = (game_Display_Size[0] // 2, game_Display_Size[1] - 50)
    move = 0

    bola = pygame.image.load('sprites/bola.png')
    bola_pos = bola.get_rect()
    bola_pos.center = (game_Display_Size[0] // 2, game_Display_Size[1] - 100)
    bola_move = [bola_spd, bola_spd]

    start = False

    while True:
        Display.blit(bg, (0, 0))
        Display.blit(game_Display, (20, 80))

        game_Display.fill((0, 0, 0))
        game_Display.set_colorkey((0, 0, 0))
        score = ['Score', pontos, 'HighScore', hs]

        game_Display.blit(jogador, jogador_pos)

        x = 5
        y = game_Display_Size[1] - 15
        for vida in range(0, vidas):
            game_Display.blit(pygame.transform.scale(jogador, (25, 8)), (x, y))
            x += 28

        tam = 20
        y = 20
        x = 50
        for sc in score:
            sc_pos = escreve(str(sc), tam, (255, 255, 255), True)
            if sc == score[2]:
                x = 150
                y = 20
            sc_pos[1].x = x
            sc_pos[1].y = y
            if sc == score[1] or sc == score[3]:
                sc_pos[1].topright = (x, y)
            Display.blit(sc_pos[0], sc_pos[1])
            x += sc_pos[1].width
            y += 20

        colisoes = []
        y = 50
        for barras in cores.values():
            barra = pygame.transform.scale(barras, ((game_Display_Size[0]) // barra_qtd, 20))
            barra_col = barra.get_rect()
            x = 0
            for retangulo in range(0, barra_qtd):
                if (x, y, barra_col.width, barra_col.height) not in remover:
                    game_Display.blit(barra, (x, y))
                    colisoes.append(pygame.Rect(x, y, barra_col.width, barra_col.height))
                x += barra_col.width
            y += 20

        for event in pygame.event.get():
            if event.type == QUIT:
                check_quit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    move = spd
                if event.key == K_LEFT:
                    move = -spd
                if event.key == K_UP:
                    if not start:
                        if move > 0:
                            bola_move[0] = bola_spd
                            start = True
                        if move < 0:
                            bola_move[0] = -bola_spd
                            start = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    check_quit()
                if event.key == K_RIGHT and move == spd or event.key == K_LEFT and move == -spd:
                    move = 0

        if len(remover) == barra_qtd * 5:
            vitoria()

        if vidas == 0:
            game_over()

        jogador_pos.x += move
        colisoes.append(jogador_pos)

        if jogador_pos.right >= game_Display_Size[0]:
            jogador_pos.right = game_Display_Size[0]
        if jogador_pos.left <= 0:
            jogador_pos.left = 0

        if start:
            bola_pos.x += bola_move[0]
            for col in colisoes:
                if bola_pos.colliderect(col):
                    if bola_move[0] > 0:
                        bola_pos.right = col.left
                        bola_move[0] = -bola_spd
                    else:
                        bola_pos.left = col.right
                        bola_move[0] = bola_spd
                    if col != jogador_pos:
                        remover.append(col)
                        pontos += 10
            bola_pos.y += bola_move[1]
            for col in colisoes:
                if bola_pos.colliderect(col):
                    if bola_move[1] > 0:
                        bola_pos.bottom = col.top
                        bola_move[1] = -bola_spd
                    else:
                        bola_pos.top = col.bottom
                        bola_move[1] = bola_spd
                    if col != jogador_pos:
                        remover.append(col)
                        pontos += 10

            if bola_pos.right > game_Display_Size[0]:
                bola_move[0] = -bola_spd
            if bola_pos.left < 0:
                bola_move[0] = bola_spd
            if bola_pos.top > Display_Size[1]:
                vidas -= 1
                start = False
            if bola_pos.y < 0:
                bola_move[1] = bola_spd

        if pontos > hs:
            hs = pontos

        game_Display.blit(bola, bola_pos)

        if not start:
            bola_pos.center = (jogador_pos.centerx, jogador_pos.top - bola_pos.height // 2)

        pygame.display.update()
        Clock.tick(60)


def game_over():
    global vidas, pontos, bola_spd

    tela_size = [Display_Size[0] - 60, Display_Size[1] - 100]
    tela = pygame.Surface(tela_size)
    tela.fill((50, 50, 50))
    opcoes = ['Game Over', 'Tentar Novamente', 'Sair']
    while True:
        Display.blit(tela, (30, 70))

        colisoes = []
        x = 65
        for op in opcoes:
            if op == opcoes[0]:
                tam = 50
            else:
                tam = 30
            texto = escreve(op, tam, (255, 255, 255), antialias=True)
            if op == opcoes[0]:
                texto[1].center = (tela_size[0] // 2, tela_size[1] // 2 - 20)
                tela.blit(texto[0], texto[1])
            else:
                y = tela_size[1] - 100
                tela.blit(texto[0], (x, y))
                colisoes.append(pygame.Rect(x, y, texto[1].width, texto[1].height))
                x += x + texto[1].width

        for event in pygame.event.get():
            if event.type == QUIT:
                check_quit()
            if event.type == MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                mouse_pos = pygame.Rect(mouse[0] - 30, mouse[1] - 70, 1, 1)
                for col in colisoes:
                    if mouse_pos.colliderect(col):
                        if col == colisoes[0]:
                            vidas = 5
                            pontos = 0
                            bola_spd = 5
                            game_loop()
                        if col == colisoes[1]:
                            check_quit()

        pygame.display.update()
        Clock.tick(60)


def vitoria():
    global bola_spd
    bola_spd += 1
    tela_size = [Display_Size[0] - 60, Display_Size[1] - 100]
    tela = pygame.Surface(tela_size)
    tela.fill((50, 50, 50))
    opcoes = ['Você Ganhou!', 'Continuar', 'Sair']
    while True:
        Display.blit(tela, (30, 70))

        colisoes = []
        x = 100
        for op in opcoes:
            if op == opcoes[0]:
                tam = 50
            else:
                tam = 30
            texto = escreve(op, tam, (255, 255, 255), antialias=True)
            if op == opcoes[0]:
                texto[1].center = (tela_size[0] // 2, tela_size[1] // 2 - 20)
                tela.blit(texto[0], texto[1])
            else:
                y = tela_size[1] - 100
                tela.blit(texto[0], (x, y))
                colisoes.append(pygame.Rect(x, y, texto[1].width, texto[1].height))
                x += x + texto[1].width

        for event in pygame.event.get():
            if event.type == QUIT:
                check_quit()
            if event.type == MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                mouse_pos = pygame.Rect(mouse[0] - 30, mouse[1] - 70, 1, 1)
                for col in colisoes:
                    if mouse_pos.colliderect(col):
                        if col == colisoes[0]:
                            game_loop()
                        if col == colisoes[1]:
                            check_quit()

        pygame.display.update()
        Clock.tick(60)


def check_quit():
    f = open('highscore.txt', 'w')
    f.write(str(hs))
    f.close()
    pygame.quit()
    quit()


if __name__ == '__main__':
    game_loop()
