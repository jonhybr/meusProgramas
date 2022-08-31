lista1 = []
lista2 = []
lista3 = []
while True:
    num = int(input('Me diga um Número: '))
    lista1.append(num)
    if num % 2 == 0:
        lista2.append(num)
    else:
        lista3.append(num)
    opc = str(input('Quer continuar? [S/N] : ')).lower().strip()
    while opc not in 'sn':
        opc = str(input('Não entendi sua resposta. Quer continuar? [S/N] : ')).lower().strip()
    if opc == 'n':
        break
print('=-'*(18 + len(lista1)))
print(f'Você digitou os números: {lista1}')
print(f'Os Números pares são: {lista2}')
print(f'E os Números ímpares são: {lista3}')
print('-='*(18 + len(lista1)))
