import pygame
from pygame.locals import *

pygame.init()

Display_Size = (500, 400)
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()
dinheiro = 0


def escreve(texto, tam=15, cor=(0, 0, 0), antialias=False):
    font = pygame.font.SysFont('calibri', tam)
    text = font.render(texto, antialias, cor)
    pos = text.get_rect()
    return text, pos


loja = pygame.Surface((200, 400))
loja.fill((100, 100, 100))
loja_nome = escreve('LOJA', 30, (20, 20, 20), antialias=True)
loja_nome[1].center = (400, 30)

opcoes = [{'Nome': 'Trabalhador', 'Quantidade': 0, 'Preço': 5, 'Lucro': 2},
          {'Nome': 'Fazenda', 'Quantidade': 0, 'Preço': 100, 'Lucro': 5},
          {'Nome': 'Fabrica', 'Quantidade': 0, 'Preço': 1000, 'Lucro': 15},
          {'Nome': 'Usina', 'Quantidade': 0, 'Preço': 5000, 'Lucro': 50}]

dps = 0
click = 1
count = 0

while True:
    Display.fill((200, 200, 200))
    Display.blit(loja, (300, 0))

    count += 1
    if count >= 60:
        dinheiro += dps
        count = 0

    clicou = False

    pontos = escreve(f'Dinheiro: {dinheiro}', 20, antialias=True)
    pontos[1].center = (120, 50)
    lucro = escreve(f'DPS: {dps} |Click: {click}', 20, antialias=True)
    lucro_pos = lucro[1].center = (70, 220)

    circulo = pygame.draw.circle(Display, (150, 80, 20), (120, 150), 50)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            clicou = True
            mouse = pygame.mouse.get_pos()
            if 70 < mouse[0] < 170 and 100 < mouse[1] < 200:
                dinheiro += click + opcoes[0]['Quantidade']
        if event.type == QUIT:
            pygame.quit()
            quit()
    y = 80
    for pos in opcoes:
        x = 305
        op = escreve(f'{pos["Nome"]}: {pos["Quantidade"]}', 15, (30, 30, 30), antialias=True)
        Display.blit(op[0], (x, y))
        opc = escreve(f'Comprar: {pos["Preço"]}', 15, (30, 30, 30), antialias=True)
        Display.blit(opc[0], (405, y))
        if clicou:
            mouse = pygame.mouse.get_pos()
            if 405 < mouse[0] < 491 and y < mouse[1] < y + 14:
                if dinheiro >= pos['Preço']:
                    dinheiro -= pos['Preço']
                    pos['Quantidade'] += 1
                    if pos['Nome'] == 'Trabalhador':
                        pos['Preço'] += pos['Preço'] // 5
                        click += pos['Lucro']
                    if pos['Nome'] == 'Fazenda':
                        pos['Preço'] += pos['Preço'] // 4
                    if pos['Nome'] == 'Fabrica':
                        pos['Preço'] += pos['Preço'] // 3
                    if pos['Nome'] == 'Usina':
                        pos['Preço'] += pos['Preço'] // 2
                    if pos['Nome'] != 'Trabalhador':
                        dps += pos['Lucro']
        y += 30

    Display.blit(pontos[0], pontos[1])
    Display.blit(loja_nome[0], loja_nome[1])
    Display.blit(lucro[0], lucro_pos)
    pygame.display.update()
    Clock.tick(60)
