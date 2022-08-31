lista = []
for c in range(1, 6):
    lista.append(int(input(f'Me diga o {c}º valor: ')))
print('=-'*21)
print(f'O maior valor foi {max(lista)}, o menor valor foi {min(lista)}')
print('O maior valor apareceu nas posições: ', end='')
for e, l in enumerate(lista):
    if l == max(lista):
        print(e+1, end=' ')
print('\nE o menor valor apareceu nas posições: ', end='')
for e, l in enumerate(lista):
    if l == min(lista):
        print(e+1, end=' ')
print()
print('-='*21)
