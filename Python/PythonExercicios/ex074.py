from random import randint
pc = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números sorteados foram: ', end='')
for n in pc:
    print(n, end=' ')
print(f'\nO maior valor foi {max(pc)}, e o menor foi {min(pc)}')
