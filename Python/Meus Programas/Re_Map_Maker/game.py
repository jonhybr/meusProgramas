import pygame
from pygame.locals import *

pygame.init()

screen_Size = [800, 500]
display = pygame.display.set_mode(screen_Size)

Clock = pygame.time.Clock()


def img_load(sprite):
    img = pygame.image.load('sprites/' + sprite).convert()
    img = pygame.transform.scale2x(img)
    return img


lista = ['start', 'end', 'lixeira', 'lixeira_co', 'colisao', 'grama', 'terra', 'terra_e', 'terra_c', 'terra_d',
         'terra_b', 'grama_ce', 'grama_cd', 'grama_bd',
         'grama_be', 'arbusto', 'arvore_be', 'arvore_bd', 'arvore_ce', 'arvore_cd', 'flor_rosa', 'flor_roxa', 'agua',
         'agua_ce', 'agua_cd', 'agua_be',
         'agua_bd', 'agua_e', 'agua_c', 'agua_d', 'agua_b', 'casa_be', 'casa_p', 'casa_b', 'casa_j', 'casa_bd',
         'casa_e', 'casa_d', 'casa_m', 'teto', 'teto2',
         'tijolo', 'parede_vertical', 'parede_horizontal', 'parede_cd', 'parede_bd', 'parede_be', 'parede_ce']

sprites = {}
for item in range(0, len(lista)):
    sprites[lista[item]] = img_load(lista[item] + '.png')


def loader(path):
    try:
        f = open(path + '.txt', 'r')
        arq = f.read()

    except ValueError:
        print('Mapa nao econtrado ou nao existe!')
        return

    except FileNotFoundError:
        print('Mapa nao econtrado ou nao existe!')
        return

    mapa_final = []
    linhas = []
    sprite = ''
    for i in arq:
        if i != '\n':
            if i == ',':
                if sprite != '':
                    linhas.append(sprite)
                    sprite = ''
            else:
                sprite += i
        if i == '\n':
            mapa_final.append(linhas.copy())
            linhas.clear()

    mapa_final.append(linhas.copy())
    return mapa_final


class Map:
    def __init__(self):
        self.mapxi = 0
        self.mapyi = 0
        self.block_size = 50
        self.zoom = 0
        self.zoomSpeed = 1
        self.tiles = loader("texto")
        self.collisions = loader("colisoes")

    def draw(self, scroll):
        self.block_size += self.zoom
        py = 0
        for y in self.tiles:
            px = 0
            for x in y:
                if x != '0':
                    tile = pygame.transform.scale(sprites[x], (self.block_size, self.block_size))
                    display.blit(tile, (px * self.block_size + scroll[0], py * self.block_size + scroll[1]))
                px += 1
            py += 1

    def zoomPlus(self):
        self.zoom = self.zoomSpeed

    def zoomMinus(self):
        self.zoom = -self.zoomSpeed

    def zoomStop(self):
        self.zoom = 0


class Player:
    def __init__(self, surface):
        self.surface = surface
        self.size = [28, 28]
        self.sprite = pygame.Surface((self.size[0], self.size[1]))
        self.pos = self.sprite.get_rect(center=(screen_Size[0] // 2, screen_Size[1] // 2))
        self.color = (150, 255, 150)
        self.inventory = [sprites['grama']]
        self.inventory_open = -1
        self.inventory_surface = pygame.Surface((500, 300))
        self.inventory_surface_pos = self.inventory_surface.get_rect(center=(screen_Size[0] // 2, screen_Size[1] // 2))

    def draw(self):
        self.sprite.fill(self.color)
        self.surface.blit(self.sprite, (self.pos[0], self.pos[1]))

    def open_inventory(self):
        self.inventory_open *= -1

    def draw_inventory(self):
        self.inventory_surface.set_alpha(200)

        self.surface.blit(self.inventory_surface, self.inventory_surface_pos)
        py = 0
        px = 0
        for y in self.inventory:
            if (px * 42) + 20 + 32 > 500:
                py += 2
                px = 0
            self.inventory_surface.blit(y, ((px * 42) + 20, (py * 32) + 20))
            px += 1


class Scroll:
    def __init__(self):
        self.pos = [0, 0]
        self.move_x = 0
        self.move_y = 0
        self.speed = 4
        self.direction_x = None
        self.direction_y = None

    def check_collision(self, mapa, player):
        py = 0
        for y in mapa:
            px = 0
            for x in y:
                if x == '1':
                    if player[0] + 32 > px * 32 + self.pos[0] and px * 32 + self.pos[0] + 32 > player[0] and \
                            player[1] + 32 > py * 32 + self.pos[1] and py * 32 + self.pos[1] + 32 > player[1]:
                        return "colidiu"
                px += 1
            py += 1

    def run(self, mapa, player):

        if self.move_x != 0:
            self.pos[0] += self.move_x
            colisao = self.check_collision(mapa, player)
            if colisao:
                self.pos[0] -= self.move_x

        if self.move_y != 0:
            self.pos[1] += self.move_y
            colisao = self.check_collision(mapa, player)
            if colisao:
                self.pos[1] -= self.move_y

    def move_right(self):
        self.move_x = -self.speed
        self.direction_x = 'right'

    def move_left(self):
        self.move_x = self.speed
        self.direction_x = 'left'

    def move_down(self):
        self.move_y = -self.speed
        self.direction_y = 'down'

    def move_up(self):
        self.move_y = self.speed
        self.direction_y = 'up'

    def stop_right(self):
        if self.direction_x == 'right':
            self.move_x = 0

    def stop_left(self):
        if self.direction_x == 'left':
            self.move_x = 0

    def stop_down(self):
        if self.direction_y == 'down':
            self.move_y = 0

    def stop_up(self):
        if self.direction_y == 'up':
            self.move_y = 0


class Game:
    def __init__(self):
        self.mapa_atual = Map()
        self.player = Player(display)
        self.scroll = Scroll()

        self.controls = {KEYDOWN: {100: self.scroll.move_right, 97: self.scroll.move_left,
                                   115: self.scroll.move_down, 119: self.scroll.move_up,
                                   61: self.mapa_atual.zoomPlus, 45: self.mapa_atual.zoomMinus},
                         KEYUP: {100: self.scroll.stop_right, 97: self.scroll.stop_left,
                                 115: self.scroll.stop_down, 119: self.scroll.stop_up,
                                 61: self.mapa_atual.zoomStop, 45: self.mapa_atual.zoomStop,
                                 101: self.player.open_inventory}}

    def run(self):

        start = True
        while start:

            display.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN and event.key in self.controls[KEYDOWN]:
                    self.controls[KEYDOWN][event.key]()

                if event.type == KEYUP and event.key in self.controls[KEYUP]:
                    self.controls[KEYUP][event.key]()

            self.mapa_atual.draw(self.scroll.pos)
            self.scroll.run(self.mapa_atual.collisions, self.player.pos)
            self.player.draw()

            if self.player.inventory_open == 1:
                self.player.draw_inventory()

            pygame.display.flip()
            Clock.tick(70)


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
