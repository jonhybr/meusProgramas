num1 = int(input('\033[1:30mPrimeiro Número: \033[m'))
num2 = int(input('\033[1:30mSegundo Número: \033[m'))
print('\033[1:30m--\033[m' * 14)
start = True
from time import sleep
while start:
    print('\033[34m|Escolha uma opção abaixo|\n|para os Números = {} e {} |\033[m'.format(num1, num2))
    print('''\033[1:36m[1]\033[m - \033[1:32mSomar\033[m
\033[1:36m[2]\033[m - \033[1:32mSubtrair\033[m
\033[1:36m[3]\033[m - \033[1:32mMultiplicar\033[m
\033[1:36m[4]\033[m - \033[1:32mDividir\033[m
\033[1:36m[5]\033[m - \033[1:32mMaior\033[m
\033[1:36m[6]\033[m - \033[1:32mEscolher novos Números\033[m
\033[1:36m[7]\033[m - \033[1:32mSair\033[m''')
    print('\033[1:30m--\033[m' * 14)
    opção = str(input('\033[1:35mOPÇÃO:\033[m '))
    print('--' * 14)
    if opção == '1':
        resultado = num1 + num2
        print('A Soma é: {}'.format(resultado))
        print('--' * 14)
        sleep(2)
    elif opção == '2':
        resultado = num1 - num2
        print('A Subtração é: {}'.format(resultado))
        sleep(2)
    elif opção == '3':
        resultado = num1 * num2
        print('A Multiplicação é: {}'.format(resultado))
        sleep(2)
    elif opção == '4':
        resultado = num1 / num2
        print('A Divisão é: {:.2f}'.format(resultado))
        print('--' * 14)
        sleep(2)
    elif opção == '5':
        if num1 == num2:
            print('Os dois tem a mesma quantidade.')
        if num1 > num2:
            resultado = num1
            print('O maior Número é {}'.format(resultado))
        elif num2 > num1:
            resultado = num2
            print('O maior Número é {}'.format(resultado))
        print('--' * 14)
    elif opção == '6':
        num1 = int(input('\033[1:30mPrimeiro Número: \033[m'))
        num2 = int(input('\033[1:30mSegundo Número: \033[m'))
    elif opção == '7':
        print('Tenha um Bom Dia!')
        start = False
    else:
        print('Não entendi digite novamente!')
        print('--'*14)
