import random

n1 = (input('Primeira pessoa:'))
n2 = (input('Segunda pessoa:'))
n3 = (input('terceira pessoa:'))
n4 = (input('quarta pessoa:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem dos alunos que vão se apresentar é: {}'.format(lista))
