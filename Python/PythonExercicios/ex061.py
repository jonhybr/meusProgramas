prim = int(input('O primeiro termo é: '))
razão = int(input('A razão é: '))
fim = 0
while fim < 10:
    print('{} ->'.format(prim), end=' ')
    prim += razão
    fim += 1
print('Fim')
