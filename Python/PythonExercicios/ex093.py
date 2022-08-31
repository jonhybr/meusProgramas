disc = {}
disc['Nome'] = str(input('O nome do Jogador é: '))
partidas = int(input('Jogou quantas partidas: '))
marcou = []
gols = 0
for c in range(0, partidas):
    gol = int(input(f'Na {c + 1}ª partida marcou: '))
    marcou.append(gol)
    gols += gol
disc['gols'] = gols
print(f'{disc["Nome"]} jogou {partidas} partidas e fez {disc["gols"]} gols')
