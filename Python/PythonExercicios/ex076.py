lista = ('leite', 5.00, 'açucar', 10, 'café', 6, 'suco', 0.50, 'nescau', 6, 'traquinas', 3)
print('=-'*17)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<25}', end='')
    else:
        print(f'R${lista[c]:>6.2f}')
print('-='*17)
