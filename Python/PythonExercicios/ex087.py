num = [[], [], [], []]
for c in range(1, 10):
    numb = int(input(f'O {c}º Número é: '))
    if numb % 2 == 0:
        num[3].append(numb)
    if c < 4:
        num[0].append(numb)
    if 7 > c > 3:
        num[1].append(numb)
    if 10 > c > 6:
        num[2].append(numb)
tot = num[3][0]
for c in range(0, len(num[3])):
    if c+1 < len(num[3]):
        tot += num[3][c+1]

print('=-'*25)
print(' '*16, f'[ {num[0][0]} ][ {num[0][1]} ][ {num[0][2]} ]')
print(' '*16, f'[ {num[1][0]} ][ {num[1][1]} ][ {num[1][2]} ]')
print(' '*16, f'[ {num[2][0]} ][ {num[2][1]} ][ {num[2][2]} ]')
print('  '*25)
print(f'A soma de todos os Números pares é: {tot}')
print(f'A soma dos Números da terceira coluna é: {num[0][2]+num[1][2]+num[2][2]}')
print(f'O maior Número digitado na segunda linha foi: {max(num[1])}')
print('=-'*25)
