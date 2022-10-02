def ficha(nome='<Desconhecido>', gol=0):
    print(f'O Jogador {nome} fez {gol} gol(s) na partida.')


jogador = str(input('Nome do jogador: '))
gols = input('Quantos gols marcou: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)
