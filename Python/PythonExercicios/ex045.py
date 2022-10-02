import random
from time import sleep

print('Vamos jogar jokenpô!')
print('Escreva : 1 - Pedra / 2 - Tesoura / 3 - Papel')
bot = random.randint(1, 3)

player = str(input('Ecolha: ')).lower()

print('Jó...', end=' '), sleep(0.8), print('Ken...', end=' '), sleep(0.8), print('Po!'), sleep(0.8)

if player == '1' and bot == 2 or player == '2' and bot == 3 or player == '3' and bot == 1:
    ved = 1
elif player == '1' and bot == 1 or player == '2' and bot == 2 or player == '3' and bot == 3:
    ved = 3
else:
    ved = 2

if bot == 1:
    bot = 'Pedra'
elif bot == 2:
    bot = 'Tesoura'
elif bot == 3:
    bot = 'Papel'
if player == '1':
    player = 'Pedra'
elif player == '2':
    player = 'Tesoura'
elif player == '3':
    player = 'Papel'
print('-='*10)
print('\033[34mJogador\033[m:', player, '\n\033[34mComputador\033[m:', bot,)
print('-='*10)
if ved == 1:
    print('\033[1;32mO jogador ganhou!')
elif ved == 2:
    print('\033[1;31mO Computador ganhou!')
elif ved == 3:
    print('\033[1;33mEmpatou!')