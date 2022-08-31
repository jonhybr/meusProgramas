from random import randint
jogo = True
erros = 0
maior = menor = num = randint(0, 10)
while jogo:
    jogador = int(input('\033[34mEscolha um número entre 0 até 10:\033[m '))
    if jogador == num:
        print('-='*18)
        print('\033[1:33mO jogador acertou! O Número era {}.\nForam necessarias: {} tentativas\033[m'.format(jogador, erros + 1))
        jogo = False
    elif jogador != num:
        erros += 1
        if jogador < num:
            print('\033[1:31mAcho que \033[4:32mMais\033[m\033[1:31m um pouco e você teria acertado\n\033[36mTente novamente!\033[m')
            print('--' * 18)
        elif jogador > num:
            print('\033[1:31mAcho que um pouco \033[4:32mMenos\033[m\033[1:31m e você teria acertado\n\033[36mTente novamente!\033[m')
            print('--' * 18)
print('=-'*18)
