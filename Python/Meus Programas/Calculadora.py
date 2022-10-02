from commons import *

pygame.init()
pygame.display.set_caption('Calculadora')
Display_Size = [350, 450]
Display = pygame.display.set_mode(Display_Size)
Clock = pygame.time.Clock()

opcoes = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '/', '', '0', '', '=']
col_opcoes = []
opc_bord = desenhar((60, 60), (20, 20, 20))

click = False
tela = ['0']
calculo = []

while True:
    check_exit()
    Display.fill((50, 50, 50))
    Display.blit(desenhar((330, 80), (20, 20, 20)), (10, 10))
    if pos == '0' or pos == '9' or pos == '8':
        Display.blit(chao, (x, y))
    if pos == '1':
        Display.blit(parede, (x, y))
        if [x, y] not in colisao:
            colisao.append([x, y])
    if pos == '7':
        Display.blit(porta_trancada_cin, (x, y))
        if [x, y] not in colisao:
            colisao.append([x, y])
    if pos == '9':
        Display.blit(chave, (x, y))
        if [x, y] not in coletaveis:
            coletaveis.append({'Nome': 'chave', 'Pos': [x, y]})
        if pegou_chave:
            mapa[y // 32][x // 32] = '0'
    if pos == '8':
        Display.blit(porta_trancada_ama, (x, y))
        if pegou_chave and [x, y] in colisao:
            colisao.remove([x, y])
            coletaveis.append({'Nome': 'porta', 'Pos': [x, y]})
        if [x, y] not in colisao and not pegou_chave:
            colisao.append([x, y])

    space = len(tela) - 1
    for num in tela:
        resultado = escreve(num, 20, (200, 200, 200), True)
        resultado[1].midright = (320 - space * 15, 40)
        Display.blit(resultado[0], resultado[1])
        space -= 1

    x = 25
    y = 100
    op = 0
    for camada in range(0, 4):
        for linha in range(0, 4):
            Display.blit(opc_bord, (x, y))
            texto = escreve(opcoes[op], 20, (200, 200, 200), True)
            texto[1].center = (x + 30, y + 30)
            Display.blit(texto[0], texto[1])
            if [x, y] not in col_opcoes:
                col_opcoes.append([x, y, 60, 60])
            if op < len(opcoes) - 1:
                op += 1
            x += 80
        y += 80
        x = 25

    pygame.display.update()
    Clock.tick(60)
