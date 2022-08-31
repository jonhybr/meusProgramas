from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    pessoa = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - pessoa
    if idade >= 21:
        maior += 1
    elif idade >= 0:
        menor += 1
    elif idade < 0:
        print('Ainda não nasceu')
print('Tem {} maior de idade e {} menor de idade'.format(maior, menor))
