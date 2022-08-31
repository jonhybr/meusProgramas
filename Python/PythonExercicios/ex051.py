prim = int(input('Primeiro termo: '))
razão = int(input('A razão: '))
decimo = prim + (10 -1) * razão
for c in range(prim, decimo + razão, razão):
    print(c, end=' -> ')
print('FIM')
