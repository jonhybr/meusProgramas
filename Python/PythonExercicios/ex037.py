cor = {'limpa': '\033[m',
       'sulinhado': '\033[4m',
       'negrito': '\033[1m',
       'branco': '\033[1;30m',
       'roxo': '\033[1;35m',
       'verde': '\033[1;32m',
       'azulclaro': '\033[1;36m',
       'vermelho': '\033[1;31m',
       'azul': '\033[34m',
       'amarelo': '\033[1;33m'}

limpar = cor['limpa']

while True:
    num = int(input('{}Me diga um numero {}Inteiro{} e eu irei converter para você:{}'.format(cor['azul'],cor['branco'],cor['azul'],limpar)))
    print('''{}Escolha uma das opções abaixo:{}
    {}------------------------------
    1{} - {}Binário{}
    {}2{} - {}Octal{}
    {}3{} - {}Hexadecimal{}
    {}------------------------------{}'''.format(cor['verde'],limpar,cor['branco'],limpar,cor['roxo'],limpar,cor['branco'],limpar,cor['roxo'],limpar,cor['branco'],limpar,cor['roxo'],limpar,cor['branco'],limpar))
    opção = int(input('{}OPÇÃO:{} '.format(cor['amarelo'],limpar)))
    if opção == 1:
        print('{}O número {}{}{} em Binário é {}{}{}'.format(cor['azulclaro'],cor['branco'],num,cor['azulclaro'],cor['verde'], bin(num)[2:],limpar))
    elif opção == 2:
        print('{}O número {}{}{} em Octal é {}{}{}'.format(cor['azulclaro'],cor['branco'],num,cor['azulclaro'],cor['roxo'], oct(num)[2:], limpar))
    elif opção == 3:
        print('{}O número {}{}{} em Hexadecimal é {}{}{}'.format(cor['azulclaro'],cor['branco'],num,cor['azulclaro'],cor['vermelho'], hex(num)[2:],limpar))
