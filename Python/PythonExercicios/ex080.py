lista = []
for c in range(1, 6):
    num = int(input(f'Me diga o {c}º valor: '))
    if c == 1 or num > max(lista):
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print('=-'*12)
print('Você digitou os números:')
print(f'{lista}')
print('-='*12)
