import pygame, sys, random
from pygame.locals import *

pygame.init()
Display_Width = 400
Display_Height = 400
Display = pygame.display.set_mode((Display_Width, Display_Height))
pygame.display.set_caption('Snake')
Clock = pygame.time.Clock()
pontuação = 0


def main():
    startScreen()
    while True:
        game_loop()
        game_over()


def game_over():
    continued = 10
    font = pygame.font.Font('freesansbold.ttf', 50)
    font2 = pygame.font.Font('freesansbold.ttf', 15)
    texto = font.render('Continue?', True, (255, 255, 255), None)
    texto3 = font2.render('(press Enter to continue)', True, (255, 255, 255), None)
    centro = texto.get_rect()
    centro3 = texto3.get_rect()
    centro.center = (Display_Width // 2, Display_Height // 2 - 60)
    centro3.midbottom = (Display_Width // 2, Display_Height - 10)

    while True:
        if continued < 0:
            main()

        texto2 = font.render(f'{continued}', True, (255, 255, 255), None)
        centro2 = texto2.get_rect()
        centro2.center = (Display_Width // 2, Display_Height // 2)

        for event in pygame.event.get(KEYDOWN):
            if event.key == K_RETURN or event.key == K_KP_ENTER:
                return

        continued -= 1
        checkForQuit()
        Display.fill((0, 0, 0))
        Display.blit(texto2, centro2)
        Display.blit(texto, centro)
        Display.blit(texto3, centro3)
        pygame.display.update()
        Clock.tick(1)


def startScreen():
    font = pygame.font.Font('freesansbold.ttf', 50)
    font2 = pygame.font.Font('freesansbold.ttf', 25)
    texto = font.render('Snake', True, (50, 200, 50), None)
    texto2 = font2.render('Pressione Enter para iniciar', True, (255, 255, 255), None)
    centro = texto.get_rect()
    centro2 = texto2.get_rect()
    centro.center = (Display_Width // 2, Display_Height - 250)
    centro2.center = (Display_Width // 2, Display_Height - 100)

    while True:
        checkForQuit()
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == K_RETURN:
                    return

        Display.fill((0, 0, 0))
        Display.blit(texto2, centro2)
        Display.blit(texto, centro)
        pygame.display.update()


def snake(x, y):
    sprite = pygame.Surface((20, 20))
    sprite.fill((100, 185, 100))
    Display.blit(sprite, (x, y))


def fruta(x, y):
    sprite = pygame.Surface((20, 20))
    sprite.fill((185, 100, 100))
    Display.blit(sprite, (x, y))


def pontos():
    font = pygame.font.SysFont('calibri', 20)
    texto = font.render(f'Pontos: {pontuação}', True, (255, 255, 255), None)
    Display.blit(texto, (5, 5))


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


def game_loop():
    global pontuação
    Start = True
    Snake_pos = [[20, 20], [40, 20], [60, 20]]
    pontuação = 0
    velocidade_x = 20
    velocidade_y = 0
    velocidade = 20
    fx = (random.randint(10, Display_Width - 20) // 20) * 20
    fy = (random.randint(10, Display_Height - 20) // 20) * 20
    while Start:
        checkForQuit()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if velocidade_x == 0:
                    if event.key == K_RIGHT:
                        velocidade_x = velocidade
                        velocidade_y = 0
                    if event.key == K_LEFT:
                        velocidade_x = -velocidade
                        velocidade_y = 0
                elif velocidade_y == 0:
                    if event.key == K_DOWN:
                        velocidade_y = velocidade
                        velocidade_x = 0
                    if event.key == K_UP:
                        velocidade_y = -velocidade
                        velocidade_x = 0

        Snake_pos[0][0] += velocidade_x
        Snake_pos[0][1] += velocidade_y

        Display.fill((30, 55, 30))
        fruta(fx, fy)

        if Snake_pos[0][0] + 20 > Display_Width or Snake_pos[0][0] < 0 \
                or Snake_pos[0][1] + 20 > Display_Height or Snake_pos[0][1] < 0:
            return

        if Snake_pos[0][0] == fx and Snake_pos[0][1] == fy:
            Snake_pos.append([20, 20])
            pontuação += 1
            fx = (random.randint(10, Display_Width - 20) // 20) * 20
            fy = (random.randint(10, Display_Height - 20) // 20) * 20

            pygame.display.update()

        for pos in range(len(Snake_pos) - 1, 0, -1):
            Snake_pos[pos][0] = Snake_pos[pos - 1][0]
            Snake_pos[pos][1] = Snake_pos[pos - 1][1]
            snake(Snake_pos[pos][0], Snake_pos[pos][1])
            if pos > 2:
                if Snake_pos[0][0] == Snake_pos[pos][0] and Snake_pos[0][1] == Snake_pos[pos][1]:
                    return
            if fx == Snake_pos[pos][0] and fy == Snake_pos[pos][1]:
                fx = (random.randint(10, Display_Width - 20) // 20) * 20
                fy = (random.randint(10, Display_Height - 20) // 20) * 20

        checkForQuit()
        pontos()
        pygame.display.update()
        Clock.tick(15)


if __name__ == '__main__':
    main()
