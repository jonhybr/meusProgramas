start = True
mult = resultado = num = int(input('\033[34mMe diga um Número:\033[m '))
print('{}! = '.format(num), end='')
while start:
    print(mult, end='')
    mult -= 1
    if mult == 0:
        print(' = {}'.format(resultado))
        start = False
    if mult > 0:
        print('x', end='')
    resultado *= mult
