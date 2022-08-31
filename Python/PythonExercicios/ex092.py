from datetime import datetime
disc = {}
disc['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
disc['idade'] = datetime.today().year - nasc
disc['carteira'] = int(input('Número da carteira de trabalho (0 se não tiver): '))
if disc['carteira'] != 0:
    disc['contratado'] = int(input('Ano em que foi contratado: '))
    disc['saida'] = disc['contratado'] + 35 - nasc
    disc['salario'] = float(input('Seu salário é: '))
print('=-' * 12)
for k, v in disc.items():
    print(f'{k} tem o valor {v}')
