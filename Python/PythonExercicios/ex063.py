num = int(input('Quantos termos você quer mostrar? : '))
num1 = 0
num2 = 1
inicio = 0
while inicio < num:
    print('{} ->'.format(num1), end=' ')
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    inicio += 1
print('Fim')
