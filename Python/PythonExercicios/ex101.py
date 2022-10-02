from datetime import datetime


def voto(nasc):
    idade = datetime.today().year - nasc
    if idade < 18:
        return 'Não Vota'
    if idade < 65:
        return 'Voto Obrigatório'
    else:
        return 'Voto Opcional'


ano = int(input('Ano de nascimento: '))
eleição = voto(ano)
anos = datetime.today().year - ano
print(f'Com {anos} anos: {eleição}')
