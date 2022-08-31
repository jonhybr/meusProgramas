lista = []
while True:
    lista.append(int(input('Me diga um número: ')))
    opc = str(input('Quer continuar? [S/N] : ')).upper().strip()
    while opc not in 'SN':
        opc = str(input('Não entendi sua resposta. Quer continuar? [S/N] : ')).upper().strip()
    if opc == 'N':
        break
print('=-'*30)
print(f'Você digitou {len(lista)} Números')
lista.sort(reverse=True)
print(f'Os Números em ordem decrescente é: {lista}')
print('O Número 5 foi digitado.' if 5 in lista else 'O Número 5 não foi digitado.')
print('-='*30)
