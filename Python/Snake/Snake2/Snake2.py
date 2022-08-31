import pygame
from pygame.locals import *
from random import randint


class Snake:
    def __init__(self, screen, screen_size):
        self.screen = screen
        self.screen_size = screen_size
        self.head = [96, 32]
        self.body = [self.head, [64, 32], [32, 32]]
        self.width = 32
        self.height = 32
        self.speed = 6
        self.counter = self.speed
        self.direction = ''
        self.next_direction = ''
        self.sprite_direction = 270
        self.collision = False
        self.sprite_head = pygame.image.load('Snake_Head.png').convert()
        self.sprite_head.set_colorkey((0, 255, 255))
        self.sprite_body = pygame.image.load('Snake_Body.png').convert()
        self.sprite_body.set_colorkey((0, 255, 255))

    def draw(self):
        for part in self.body:
            if part == self.body[0]:
                self.screen.blit(pygame.transform.rotate(self.sprite_head, self.sprite_direction), part)
            else:
                self.screen.blit(self.sprite_body, part)
        self.counter += 1

    def change_snake_body(self):
        if len(self.body) != 1:
            for i in self.body[::-1]:
                if self.body.index(i) != 0:
                    self.body[self.body.index(i)] = self.body[self.body.index(i) - 1].copy()

    def grow(self):
        self.body.append([-100, -100])

    def move(self):
        if self.counter >= self.speed and self.direction != '':
            self.change_snake_body()
            if self.direction == 'right':
                self.head[0] += self.width
                self.sprite_direction = 270
            elif self.direction == 'left':
                self.head[0] -= self.width
                self.sprite_direction = 90
            elif self.direction == 'down':
                self.head[1] += self.height
                self.sprite_direction = 180
            elif self.direction == 'up':
                self.head[1] -= self.height
                self.sprite_direction = 0
            self.next_direction = self.direction
            self.check_colision()
            self.counter = 0

    def check_colision(self):
        # colisao corpo
        for part in self.body[1:]:
            if part == self.body[0]:
                self.collision = True
        # colisao tela
        if self.head[0] + self.width > self.screen_size[0] or self.head[0] < 0 \
                or self.head[1] + self.height > self.screen_size[1] or self.head[1] < 0:
            self.collision = True


class Apple:
    def __init__(self, surface, display_size):
        self.surface = surface
        self.width = 32
        self.height = 32
        self.sprite = pygame.image.load('Apple.png').convert()
        self.sprite.set_colorkey((0, 255, 255))
        self.pos = []
        self.count = 0
        self.create(display_size)

        self.text = Text()

    def draw(self):
        self.surface.blit(self.sprite, self.pos)

    def draw_count(self):
        font1 = self.text.font_create(30)
        text1 = font1.render(f'{self.count}', True, (0, 0, 0))
        self.surface.blit(text1, (20, 20))

    def create(self, screen_size):
        self.pos = [randint(0, screen_size[0] - self.width), randint(0, screen_size[1] - self.height)]
        creating = 0
        while creating < 2:
            creating = 0
            for ap in range(0, 2):
                if self.pos[ap] % 32 != 0:
                    self.pos[ap] -= 1
                else:
                    creating += 1


class Text:
    def __init__(self):
        self.fontBase = 'freesansbold.ttf'

    def font_create(self, size):
        return pygame.font.Font(self.fontBase, size)

    def center(self, text, display_size, x=0, y=0):
        centro = text.get_rect()
        centro.center = (display_size[0] // 2 + x, display_size[1] // 2 + y)
        return centro


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.display_Size = [800, 480]
        self.display = pygame.display.set_mode(self.display_Size)
        self.runGame = True
        self.Clock = pygame.time.Clock()

        self.background = pygame.image.load('Grama_bg.png').convert()
        self.apple = Apple(self.display, self.display_Size)
        self.snake = Snake(self.display, self.display_Size)
        self.text = Text()

    def run(self):

        game.start_screen()

        while self.runGame:

            self.display.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runGame = False
                if event.type == KEYDOWN:
                    if self.snake.direction == self.snake.next_direction:
                        if event.key == K_RIGHT and self.snake.direction != 'left':
                            self.snake.direction = 'right'
                        elif event.key == K_LEFT and self.snake.direction != 'right' and self.snake.direction != '':
                            self.snake.direction = 'left'
                        elif event.key == K_DOWN and self.snake.direction != 'up':
                            self.snake.direction = 'down'
                        elif event.key == K_UP and self.snake.direction != 'down':
                            self.snake.direction = 'up'

                if event.type == KEYUP and event.key == K_ESCAPE:
                    self.runGame = False

            if self.snake.head == self.apple.pos:
                self.apple.create(self.display_Size)
                while self.apple.pos in self.snake.body:
                    self.apple.create(self.display_Size)

                self.apple.count += 1
                self.snake.grow()

            self.apple.draw()

            self.snake.move()
            self.snake.draw()

            self.apple.draw_count()

            if self.snake.collision:
                self.game_over()

            self.Clock.tick(60)
            pygame.display.update()

    def start_screen(self):

        font1 = self.text.font_create(80)
        text1 = font1.render('Snake', True, (50, 180, 70))
        text1Center = self.text.center(text1, self.display_Size, y=-50)

        font2 = self.text.font_create(40)
        text2 = font2.render('Pressione Enter para iniciar.', True, (150, 150, 150))
        text2Center = self.text.center(text2, self.display_Size, y=50)

        start = True
        while start:
            self.display.fill((240, 240, 200))
            self.display.blit(text1, text1Center)
            self.display.blit(text2, text2Center)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == K_RETURN:
                        return

            self.Clock.tick(60)
            pygame.display.update()

    def game_over(self):

        font1 = self.text.font_create(80)
        text1 = font1.render('Fim de Jogo!', True, (220, 80, 70))
        text1Center = self.text.center(text1, self.display_Size, y=-50)

        font2 = self.text.font_create(40)
        text2 = font2.render('Pressione Enter para jogar novamente.', True, (150, 150, 150))
        text2Center = self.text.center(text2, self.display_Size, y=50)
        
        game_over = True
        while game_over:

            self.display.fill((100, 100, 100))
            self.display.blit(text1, text1Center)
            self.display.blit(text2, text2Center)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        self.runGame = False
                        return
                    if event.key == K_RETURN:
                        self.reset()
                        game_over = False

            self.Clock.tick(60)
            pygame.display.update()

    def reset(self):
        self.snake = Snake(self.display, self.display_Size)
        self.apple = Apple(self.display, self.display_Size)


if __name__ == '__main__':
    game = Game()
    game.run()
