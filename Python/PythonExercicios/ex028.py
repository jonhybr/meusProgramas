import random

numR = random.randint(0, 5)
num = int(
    input('Eu vou dizer um numero entre 0 até 5, me diga um numero e veja se consegue adivinhar qual eu escolhi:'))
if numR == num:
    print('Uau você acertou eu estava mesmo pensando no número {}'.format(num))
else:
    print('Que pena, eu estava pensando no número {} e não no {}, tente denovo'.format(numR, num))
