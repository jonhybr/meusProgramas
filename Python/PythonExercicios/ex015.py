tempo = float(input('Você alugou o carro à quantos dias?'))
carro = float(input('Você alugou o carro por {:.0f} dias e andou quantos KM?'.format(tempo)))
total = (carro * 0.15) + (tempo * 60)
print('Bom, então já que você alugou à {:.0f} dias e andou {}KM você vai pagar R${}'.format(tempo,carro,total))
