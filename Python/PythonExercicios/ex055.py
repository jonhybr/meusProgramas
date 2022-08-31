maior = 0
menor = 0
for pess in range(1,6):
    peso = float(input('O peso da {}ª em Kg é: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi {}Kg e o menor peso foi {}Kg'.format(maior, menor))
