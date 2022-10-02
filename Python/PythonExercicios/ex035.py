print('Vou lhe dizer se é possivel formar um triangulo com 3 números que você ira me dizer.')
ladoA = int(input('Primeiro número:'))
ladoB = int(input('Segundo número:'))
ladoC = int(input('Terceiro número:'))

if ladoA + ladoB > ladoC and ladoB + ladoC > ladoA and ladoA + ladoC > ladoB:
   print('Pode formar triangulo')
else:
    print('Não pode formar triangulo')