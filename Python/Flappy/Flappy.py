import pygame, random, time
from pygame.locals import *

pygame.init()
Display_Width = 500
Display_Height = 300
pygame.display.set_caption('Flappy')
Display = pygame.display.set_mode((Display_Width, Display_Height))
Clock = pygame.time.Clock()
basicFont = pygame.font.Font('freesansbold.ttf', 20)
pot = 0
sprite = pygame.image.load('bixo.png')


def main():
    startScreen()
    while True:
        game_loop()
        game_over()


def pontos(count):
    font = pygame.font.SysFont(None, 20)
    texto = font.render(f'Pontos: {count}', True, (0, 0, 0), None)
    Display.blit(texto, (5, 5))


def canos(x, y, vel):
    x += vel
    sprite = pygame.image.load('cano.png')
    Display.blit(sprite, (x, y))


def startScreen():
    titulo = pygame.font.Font('freesansbold.ttf', 50)
    texto1 = titulo.render('Flappy Game', True, (50, 185, 50), None)
    texto2 = basicFont.render('Press any key to Start', True, (255, 255, 255), None)
    centro1 = texto1.get_rect()
    centro2 = texto2.get_rect()
    centro1.midtop = (Display_Width // 2, Display_Height // 4)
    centro2.midbottom = (Display_Width // 2, Display_Height - 50)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Display.fill((0, 0, 0))
        Display.blit(texto1, centro1)
        Display.blit(texto2, centro2)
        pygame.display.update()


def game_loop():
    global pot
    y = Display_Height // 2
    x = 100
    gravidade = 0
    canospos = [[Display_Width, random.randint(-120, 0)]]
    pontuação = 0
    velocidade = -5
    start = False
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    gravidade = 1
                    for c in range(0, 5):
                        gravidade -= c
                        pygame.display.update()

            if event.type == pygame.KEYUP:
                if event.key == K_UP and gravidade == 20:
                    gravidade = 0
                if event.key == K_UP:
                    start = True

        Display.fill((160, 180, 225))

        Display.blit(pygame.transform.rotate(sprite, -gravidade), (x, y))
        if start:
            pot = pontuação

            y += gravidade

            if gravidade != 8:
                if gravidade > 8:
                    gravidade = 0
                gravidade += 1

            for c in range(0, len(canospos)):
                if canospos[c][0] == 100:
                    pontuação += 1
                if len(canospos) < 3:
                    if canospos[c][0] == Display_Width - 200:
                        canospos.append([canospos[c][0] + 200, random.randint(-120, 0)])
                if canospos[c][0] + 40 < 0:
                    if c == 0:
                        canospos[c][0] = canospos[c + 2][0] + 200
                        canospos[c][1] = random.randint(-120, 0)
                    if c != 0:
                        canospos[c][0] = canospos[c - 1][0] + 200
                        canospos[c][1] = random.randint(-120, 0)
                for b in range(0, 2):
                    if b % 2 != 0:
                        p = 180 + 80
                    else:
                        p = 0
                    canos(canospos[c][0], canospos[c][1] + p, velocidade)
                    if x + 26 > canospos[c][0] and canospos[c][0] + 40 > x:
                        if y < canospos[c][1] + 180 and p == 0 or y + 26 > canospos[c][1] + 260:
                            time.sleep(0.2)
                            return

                canospos[c][0] += velocidade

            if y + 20 > Display_Height:
                time.sleep(0.2)
                return

        pontos(pontuação)
        pygame.display.update()
        Clock.tick(30)


def game_over():
    fonte = pygame.font.Font('freesansbold.ttf', 80)
    fonte2 = pygame.font.Font('freesansbold.ttf', 30)
    fonte3 = pygame.font.Font('freesansbold.ttf', 12)
    texto = fonte.render('Game Over!', True, (185, 50, 50), None)
    texto2 = fonte2.render(f'Pontos: {pot}', True, (255, 255, 255), None)
    texto3 = fonte3.render('Pressione Enter para jogar novamente', True, (255, 255, 255), None)
    centro = texto.get_rect()
    centro2 = texto2.get_rect()
    centro3 = texto3.get_rect()
    centro.center = (Display_Width // 2, Display_Height - 200)
    centro2.center = (Display_Width // 2, Display_Height - 100)
    centro3.bottomright = (Display_Width - 4, Display_Height)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == KEYUP:
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    return

        Display.fill((0, 0, 0))
        Display.blit(texto3, centro3)
        Display.blit(texto2, centro2)
        Display.blit(texto, centro)
        pygame.display.update()


main()
