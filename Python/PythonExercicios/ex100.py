from random import randint
from time import sleep


def sorteia(a):
    print('Sorteando 5 números: ')
    for c in range(0, 5):
        num = randint(1, 10)
        a.append(num)
        print(num, end=' ')
        sleep(0.3)
    print('Fim.')


def somaPar(b):
    num = 0
    for n in b:
        if n % 2 == 0:
            num += n
    print('A soma dos números pares é:', num)


numeros = []
sorteia(numeros)
somaPar(numeros)
