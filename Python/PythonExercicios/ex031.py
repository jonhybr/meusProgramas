dist = float(input('Qual a distancia de sua viagem? (KM) :'))
preço = 0
if dist <= 200:
    preço = dist * 0.50
if dist > 200:
    preço = dist * 0.45
print('Essa viagem vai lhe custar R${}'.format(preço))
