numeros = (int(input('Me diga um número: ')), int(input('Me diga um número: ')), int(input('Me diga um número: ')), int(input('Me diga um número: ')))
print('Você digitou os números: ', end='')
for n in numeros:
    print(n, end=' ')
if 9 in numeros:
    print(f'\nVocê digitou {numeros.count(9)} vezes o número 9')
else:
    print('\nVocê não digitou o número 9')
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('Você não digitou o número 3')
print('Os números pares são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
print('')
