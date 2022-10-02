from math import hypot

cateto1 = float(input('Bora calcular triangulo me fala o comprimento de um cateto:'))
cateto2 = float(input('Agora me fala o lado do outro cateto:'))
hipotenusa = hypot(cateto1, cateto2)
print('A hipotenusa é {:.2f} viu como é fácil?'.format(hipotenusa))
