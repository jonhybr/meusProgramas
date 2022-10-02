largura = float(input('Me diga a largura de alguma parede:'))
altura = float(input('Agora me diga sua altura:'))
area = largura * altura
print('Se sua parede tem {:.3f}m² e cada litro de tinta pinta 2m², então seram necessarios {:.3f} litros de tinta'.format(area,area / 2))