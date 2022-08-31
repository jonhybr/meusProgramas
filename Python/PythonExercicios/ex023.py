num = int(input('Me diz um número ai, tem que ser entre 0 até 9999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O numero {} tem:'.format(num))
print('unidades : {}'.format(u))
print('dezenas : {}'.format(d))
print('centenas : {}'.format(c))
print('milhares : {}'.format(m))
