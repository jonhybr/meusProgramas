lista = []
while True:
    num = int(input('Me diga um Número: '))
    if num not in lista:
        lista.append(num)
    opc = str(input('Quer continuar? [S/N] : ')).upper().strip()
    while opc not in 'SN':
        opc = str(input('Não entendi sua resposta. Quer continuar? [S/N] : ')).upper().strip()
    if opc == 'N':
        break
print('=-'*12)
print(f'Você digitou os números:')
print(sorted(lista))
print('-='*12)
