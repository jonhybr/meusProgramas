disc = {}
lis = []

while True:
    disc['nome'] = str(input('O nome é: '))
    disc['sexo'] = str(input('O sexo é (M/F): '))
    disc['idade'] = int(input('A idade é: '))
    lis.append(disc.copy())
    sair = str(input('Quer continuar? [S/N] '))
    if sair in 'nN':
        break

print(f'Foram cadastradas {len(lis)} pessoas')
media = 0
for c in range(0, len(lis)):
    media += lis[c]['idade']
media = media / (len(lis))
print(f'A media de idade é {media} e as pessoas acima da média são: ')
for n in range(0, len(lis)):
    if lis[n]['idade'] > media:
        print(lis[n]['nome'], end=' ')
print()
print('As mulheres que foram cadastradas são: ')
for f in range(0, len(lis)):
    if lis[f]['sexo'] in 'fF':
        print(lis[f]['nome'], end=' ')

