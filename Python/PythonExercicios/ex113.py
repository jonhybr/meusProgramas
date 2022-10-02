def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('Erro! digite um número inteiro valido.')
        else:
            return n


def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('Erro! Digite um número Real valido.')
        else:
            return n


num = leiaInt('Me diga um número inteiro: ')
print(f'Você digitou o número {num}')

num2 = leiaFloat('Me diga um número Real: ')
print(f'Você digitou o número {num2}')
