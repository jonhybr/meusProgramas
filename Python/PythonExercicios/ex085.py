num = [[], []]
for c in range(1, 8):
    numb = int(input(f'Me diga o {c}º Número: '))
    if numb % 2 == 0:
        num[0].append(numb)
    else:
        num[1].append(numb)
print(f'Os Números pares foram: {sorted(num[0])}\nOs Números ímpares foram: {sorted(num[1])}')
