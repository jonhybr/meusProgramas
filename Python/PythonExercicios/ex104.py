def leiaInt(frase):
    while True:
        num = str(input(frase))
        if not num.isnumeric():
            print('Não é um Número digite novamente: ')
        else:
            return num


n = leiaInt('Digite um Número: ')
print(f'O numero é {n}')
