from random import randint
from time import sleep
dados = {}
valores = []
for c in range(0, 6):
    valores.append(randint(1, 6))
dados['valores'] = valores
print(dados)