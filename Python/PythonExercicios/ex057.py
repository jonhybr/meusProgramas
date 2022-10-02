start = True
while start:
    sexo = str(input('Me diga seu sexo (M/F): ')).lower().strip()[0]
    if sexo == '':
        print('Não entendi sua resposta digite novamente')
    elif sexo in 'mf':
        start = False
    else:
        print('Não entendi sua resposta digite novamente')
