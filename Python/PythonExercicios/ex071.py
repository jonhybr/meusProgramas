print('Olá eu sou seu caixa eletrônico')
while True:
    valor = int(input('Quanto você quer sacar? : '))
    break
print('O caixa sacou:')
if valor // 50 > 0:
    print('{} Cédulas de 50'.format(valor // 50))
if valor % 50 != 0:
    valor20 = (valor % 50) // 20
    if valor20 > 0:
        print('{} Cédulas de 20'.format(valor20))
if (valor % 50) % 20 != 0:
    valor10 = (valor % 50) % 20 // 10
    if valor10 > 0:
        print('{} Cédulas de 10'.format(valor10))
if ((valor % 50) % 20) % 10:
    valor1 = ((valor % 50) % 20) % 10 // 1
    if valor1 > 0:
        print('{} Cédulas de 1'.format(valor1))
