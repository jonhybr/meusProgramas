from random import randint
from time import sleep
jogos = []
num = int(input('Quantos jogos você quer sortear?: '))
for c in range(0, num):
    jogos.append([])
    for p in range(0, 6):
        if c < len(jogos):
            random = randint(1, 60)
            while random in jogos[c]:
                random = randint(1, 60)
            jogos[c].append(random)
print(f'\033[1:34m{"|Gerando Números|":=^34}\033[m')
for c in range(0, num):
    print(f'\033[33m{c+1}º Jogo:\033[m', '\033[36m', sorted(jogos[c]))
    sleep(1)
print(f'\033[1:34m{"|Números Sorteados!|":=^34}\033[m')
