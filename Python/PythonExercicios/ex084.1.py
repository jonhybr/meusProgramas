pessoas = [[], [], [], [], [], []]
while True:
    pessoas[0].append(str(input('Nome: ')))
    pessoas[1].append(float(input('Peso: ')))
    if len(pessoas[0]) == 1:
        pessoas[4].append(pessoas[0][0])
        pessoas[5].append(pessoas[0][0])
        pessoas[2].append(pessoas[1][0])
        pessoas[3].append(pessoas[1][0])
    if len(pessoas[0]) > 1:
        if pessoas[1][0] == pessoas[2][0]:
            pessoas[4].append(pessoas[0][len(pessoas[0])-1])
        if pessoas[1][0] == pessoas[3][0]:
            pessoas[5].append(pessoas[0][len(pessoas[0])-1])
    if pessoas[1][0] > pessoas[2][0]:
        pessoas[2].clear()
        pessoas[2].append(pessoas[1][len(pessoas[1])-1])
        pessoas[4].clear()
        pessoas[4].append(pessoas[0][len(pessoas[0])-1])
    if pessoas[1][0] < pessoas[3][0]:
        pessoas[3].clear()
        pessoas[3].append(pessoas[1][len(pessoas[1])-1])
        pessoas[5].clear()
        pessoas[5].append(pessoas[0][len(pessoas[0])-1])
    opc = str(input('Quer continuar? [S/N]: ')).strip().lower()
    while opc not in 'sn':
        opc = str(input('Quer continuar? [S/N]: ')).strip().lower()
    if opc == 'n':
       break
    pessoas[1].clear()
print(f'Você cadastrou {len(pessoas[0])} pessoas.\nO maior peso foi {pessoas[2][0]} e foram:')
for c in pessoas[4]:
    print(f'|{c}|', end=' ')
print(f'\nO menor peso foi {pessoas[3][0]} e foram: ')
for c in pessoas[5]:
    print(f'|{c}|', end=' ')
