num = int(input('\033[34mMe diga um Número e eu direi seu fatorial:\033[m '))
print('{}! = {} x '.format(num, num), end='')
for c in range(num - 1, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    num *= c
print('{}'.format(num))
