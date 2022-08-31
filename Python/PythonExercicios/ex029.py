velocidade = int(input('Seu carro está andando a que velocidade? (KM/h) :'))
if velocidade > 80:
    multa = (-80 + velocidade) * 7
    print('Você está acima do limite de velocidade terá que pagar R${} de multa'.format(float(multa)))
else:
    print('Você está abaixo do limite de velocidade')

if velocidade == 80:
    print('Tome cuidado você está no limite maximo ')

