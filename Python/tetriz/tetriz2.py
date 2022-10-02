import pygame
from pygame.locals import *
from random import randint

pygame.init()


class Blocks:
    def __init__(self):
        self.colors = {'o': 'yellow', 's': 'green', 'z': 'red', 'i': 'cyan', 'l': 'orange', 'r': 'blue', 't': 'purple'}

        self.s = [['0', '0', '0'],
                  ['0', '1', '1'],
                  ['1', '1', '0']]

        self.z = [['0', '0', '0'],
                  ['1', '1', '0'],
                  ['0', '1', '1']]

        self.l = [['0', '1', '0'],
                  ['0', '1', '0'],
                  ['0', '1', '1']]

        self.r = [['0', '1', '0'],
                  ['0', '1', '0'],
                  ['1', '1', '0']]

        self.o = [['1', '1'],
                  ['1', '1']]

        self.i = [['0', '1', '0', '0'],
                  ['0', '1', '0', '0'],
                  ['0', '1', '0', '0'],
                  ['0', '1', '0', '0']]

        self.t = [['0', '0', '0'],
                  ['0', '1', '0'],
                  ['1', '1', '1']]

    def get_format(self, shape):
        formats = {0: self.s, 1: self.o, 2: self.l,
                   3: self.r, 4: self.t, 5: self.i,
                   6: self.z}

        return formats[shape]


class Player:
    def __init__(self, surface, size):
        self.surface = surface
        self.blocks = Blocks()
        self.size = size
        self.block = []
        self.stopped_blocks = []
        self.block_sprite = pygame.Surface(self.size)
        self.block_sprite.fill((255, 255, 255))

    def add_block(self):
        block_format = randint(0, 6)
        pos = [5, -3]

        shape = self.blocks.get_format(block_format)

        new_block = []
        new_pos = pos.copy()
        for y in shape:
            new_pos[0] = pos[0]
            for x in y:
                if x == '1':
                    new_block.append(new_pos.copy())
                new_pos[0] += 1
            new_pos[1] += 1

        self.block = new_block

    def draw(self, sprite, tiles):
        for tile in tiles:
            self.surface.blit(sprite, ((tile[0] * self.size[0]) + 130, (tile[1] * self.size[1]) + 100))

    # Checa se o jogador fez uma linha
    def check_win(self):
        count = 0
        win = []
        for pos in self.stopped_blocks:
            for i in self.stopped_blocks:
                if pos[1] == i[1]:
                    count += 1
            if count == 10:
                win.append(pos)
            count = 0

        if len(win) >= 10:
            self.tetriz(win)

    # O que ocorre quando faz uma ou mais linhas
    def tetriz(self, values):
        move = len(values) // 10
        for row in values:
            self.stopped_blocks.remove(row)
        for block in self.stopped_blocks:
            block[1] += move

    def rotate(self, keypressed):
        new_shape = self.block.copy()
        for i in range(0, 8):
            print('a')

    def move(self, keypressed):
        direction = {K_LEFT: [0, -1], K_RIGHT: [0, 1], K_DOWN: [1, 1]}
        for tile in self.block:
            tile[direction[keypressed][0]] += direction[keypressed][1]

        test_colision = self.check_collision(direction[keypressed])
        if test_colision:
            for tile in self.block:
                tile[direction[keypressed][0]] -= direction[keypressed][1]

    def check_collision(self, move):
        colision = [False, 'any', None]
        colided = []
        for tile in self.block:
            # Colidiu com a tela
            if tile[0] < 0 or tile[0] > 9:
                colision = [True, 'x']

            # Colidiu com o chao
            if tile[1] == 26:
                for groundTile in self.block:
                    colided.append(groundTile.copy())
                colision = [True, 'y', colided]

            # Colidiu com outro bloco
            if tile in self.stopped_blocks:
                for hitTile in self.block:
                    colided.append(hitTile.copy())
                colision = [True, 'any', colided]

        if colision[0]:
            # Colisao horizontal
            if colision[1] == 'x':
                return True

            if colision[1] == 'any' and move[0] == 0:
                return True

            # Colisao vertical
            if colision[1] == 'y' or colision[1] == 'any':
                if move[0] == 1:
                    for tile in colision[2]:
                        tile[move[0]] -= move[1]
                    self.stopped_blocks.extend(colision[2])
                    self.check_win()
                    self.add_block()

        return False


class Game:
    def __init__(self):
        self.screen_size = [450, 660]
        self.screen = pygame.display.set_mode(self.screen_size)
        self.grid_size = (10, 25)
        self.tile_size = (20, 20)

        self.player = Player(self.screen, self.tile_size)
        self.blocks = Blocks()

        self.mapblock = pygame.Surface(self.tile_size)
        self.mapblock.fill((50, 50, 50))

        self.time = 0
        self.speed = 20
        self.Clock = pygame.time.Clock()

    def draw_grid(self, sprite):
        for y in range(self.grid_size[1], 0, -1):
            for x in range(0, self.grid_size[0]):
                self.screen.blit(sprite, ((x * self.tile_size[0]) + 130, (y * self.tile_size[1]) + 100))

    def run(self):

        running = True

        controls = {K_LEFT: self.player.move, K_RIGHT: self.player.move,
                    K_DOWN: self.player.move, K_r: self.player.rotate}

        while running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

                if event.type == KEYUP:
                    if event.key == K_UP:
                        self.player.add_block()
                    if event.key in controls:
                        controls[event.key](event.key)

            self.draw_grid(self.mapblock)
            self.player.draw(self.player.block_sprite, self.player.stopped_blocks)
            self.player.draw(self.player.block_sprite, self.player.block)

            if self.time >= self.speed:
                self.player.move(K_DOWN)
                self.time = 0

            self.time += 1
            pygame.display.flip()
            self.Clock.tick(30)


if __name__ == '__main__':
    game = Game()
    game.run()
