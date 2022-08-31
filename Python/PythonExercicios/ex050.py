num = 0
resultado = 0
for c in range(1, 7):
    num = int(input('Escolha o {}° Número: '.format(c)))
    if num % 2 == 0:
        resultado += num
print('')
if resultado > 0:
    print('A soma de todos os Números pares foi:', resultado)
else:
    print('Você não escolheu nenhum Número par')