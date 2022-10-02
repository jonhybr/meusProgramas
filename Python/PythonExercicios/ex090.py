pessoas = {}
pessoas['Nome'] = str(input('O nome do aluno é: '))
pessoas['Média'] = float(input('A média é: '))
if pessoas['Média'] >= 7:
    pessoas['Situação'] = 'Aprovado'
else:
    pessoas['Situação'] = 'Reprovado'
for c, v in pessoas.items():
    print(c, 'é igual a', v)
