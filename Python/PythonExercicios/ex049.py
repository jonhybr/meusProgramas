start = True
while start:
    num = int(input('\033[34mMe diga um número e eu direi a tabuada deste número:\033[m '))
    for c in range(1, 11):
        print('\033[36m{} x {:2} \033[1:30m=\033[m \033[1:32m{}'.format(num, c, num*c))
    sair = str(input())
    if sair == 'sair':
        start = False
