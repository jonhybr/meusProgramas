start = True
while start:
    num = int(input('\033[34mMe diga um número:\033[m '))
    count = 0
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[4:32m{}\033[m'.format(c), end=' ')
            count += 1
        elif num % c != 0:
            print('\033[31m{}'.format(c), end=' ')
    print('')
    if count == 2:
        print('\033[36mO Número \033[1:33m{}\033[m\033[36m é primo pois, só foi divido \033[4:32m2\033[m \033[36mvezes.\033[m'.format(num))
    else:
        print('\033[36mO Número \033[1:33m{}\033[m\033[36m não é primo, pois foi dividido \033[4:32m{}\033[m \033[36mvezes.\033[m'.format(num, count))
