from random import randint
jogo = True
erros = 0
while jogo:
    num = randint(0, 10)
    jogador = int(input('\033[34mEscolha um número entre 0 até 10:\033[m '))
    if jogador == num:
        print('-='*18)
        print('\033[1:33mO jogador acertou! O Número era {}.\nForam necessarias: {} tentativas\033[m'.format(jogador, erros + 1))
        jogo = False
    elif jogador != num:
        erros += 1
        print('\033[1:31mO Número era {} e você escolheu {}\033[m\n\033[36mTente novamente!\033[m'.format(num, jogador))
        print('--' * 18)
print('=-'*18)
