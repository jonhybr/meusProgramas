from datetime import date
nome = str(input('Seu nome:')).strip().title()
nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc
nada = 'você é um nadador'
p = 'Parabéns!'
if idade < 10:
    print(nome, nada, 'Mirim,',p)
elif idade < 15:
    print(nome, nada, 'Infantil,',p)
elif idade < 20:
    print(nome, nada, 'Junior,',p)
elif idade < 21:
    print(nome, nada, 'Sênior,',p)
elif idade > 20:
    print(nome, nada, 'MASTER',p)