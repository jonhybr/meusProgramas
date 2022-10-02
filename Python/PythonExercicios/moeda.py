def metade(n, din=False):
    r = n / 2
    if din:
        return moeda(r)
    return r


def dobro(n, din=False):
    r = n * 2
    if din:
        return moeda(r)
    return r


def aumentar(n, p, din=False):
    r = n + (n * p / 100)
    if din:
        return moeda(r)
    return r


def diminuir(n, p, din=False):
    r = n - (n * p / 100)
    if din:
        return moeda(r)
    return r


def moeda(n):
    coisa = str(n)
    r = 'R$' + coisa
    return r


def resumo(n=0, a=0, d=0):
    print('-=' * 20)
    print(f'{"Tabela":^40}')
    print('=-' * 20)
    print(f'Número Analizado:       {n:>16}')
    print(f'O Dobro é:              {dobro(n):>16}')
    print(f'A Metade é:             {metade(n):>16}')
    print(f'O Aumento em {a}% é:    {aumentar(n, a):>17}')
    print(f'A Diminuição em {a}% é: {diminuir(n,d):>17}')
