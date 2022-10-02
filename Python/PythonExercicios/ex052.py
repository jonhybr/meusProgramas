start = True
while start:
    num = int(input('\033[34mMe diga um número e eu direi se é um número primo:\033[m '))

    if num == -1:
        start = False
    if num == 2 or num == 3:
        print('\033[32mÉ Número primo!\033[m')
    elif num % 2 == 0 or num % 3 == 0:
        print('\033[31mNâo é um Número primo\033[m')
    else:
        print('\033[32mÉ Número primo!\033[m')

