def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('Erro! digite um número inteiro valido.')
        else:
            return n


def linha(tam=20):
    return '-=' * tam


def menu(txt):
    print(linha())
    print(f'{txt:^40}')
    print(linha())


def opcoes(lista):
    menu('Menu Principal')
    for op in range(0, len(lista)):
        print(f'{op + 1} -', lista[op])
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

