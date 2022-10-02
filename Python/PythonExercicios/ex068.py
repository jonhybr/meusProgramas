from random import randint
vitorias = 0
print('=-'*13, '\n\033[33mVamos Jogar Par ou Impar!\033[m')
print('-='*13)
while True:
    pc = randint(0, 10)
    esc = int(input('\033[1:34mDigite um Número:\033[m '))
    opc = ' '
    while opc not in 'PpIi':
        opc = str(input('\033[1:34mVocê quer Par[P] ou Impar[I]? :\033[m ')).lower().strip()[0]
    if opc == 'i':
        op = 'Impar'
    elif opc == 'p':
        op = 'Par'
    if (esc + pc) % 2 == 0 and opc == 'p' or (esc + pc) % 2 != 0 and opc == 'i':
        print(f'\n\033[35mVocê escolheu {esc} e {op}, e o computador escolheu {pc}\033[m.\n\033[1:36mVocê Ganhou! Continue.\n')
        vitorias += 1
    elif (esc + pc) % 2 == 0 and opc == 'i' or (esc + pc) % 2 != 0 and opc == 'p':
        print(f'\n\033[35mVocê escolheu {esc} e {op}, e o computador escolheu {pc}.\033[m', f'\n\033[32mVocê Ganhou {vitorias} Vezes.\033[m' if vitorias > 0 else '')
        print('\n\033[1:31mGAMER OVER!')
        break
