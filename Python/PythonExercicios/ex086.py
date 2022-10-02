num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = int(input('Número: '))
print('=-'*12)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{num[l][c]:^5}]', end=' ')
    print()
print('-='*12)
