somidade = 0
hmaisv = 0
nomemv = ''
mulmv = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    pessoa = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F) : ')).lower().strip()
    somidade += idade
    if sexo == 'f' and idade < 20:
        mulmv += 1
    if p == 1 and sexo == 'm':
        hmaisv = idade
        nomemv = pessoa
    elif idade > hmaisv and sexo == 'm':
        hmaisv = idade
        nomemv = pessoa
print('\nA média de idade é {:.1f}'.format(somidade / 4))
print('O homem mais velho é {}, com {} anos.'.format(nomemv, hmaisv))
if mulmv == 0:
    print('Não tem mulheres com menos de 20 anos.')
else:
    print('Tem {} mulheres com menos de 20 anos.'.format(mulmv))
