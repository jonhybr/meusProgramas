cores = {'limpar': '\033[m',
         'azul': '\033[1;34m',
         'branco': '\033[30m',
         'roxo': '\033[1;35m',
         'amarelo': '\033[4;33m',
         'vermelho': '\033[1;31m'}
limpar = cores['limpar']

print('{}Vou lhe dizer se é possivel formar um triângulo com 3 números, que você irá me dizer.{}'.format(cores['azul'], limpar))
ladoA = float(input('{}Primeiro número:{}'.format(cores['branco'],limpar)))
ladoB = float(input('{}Segundo número:{}'.format(cores['branco'],limpar)))
ladoC = float(input('{}Terceiro número:{}'.format(cores['branco'],limpar)))

if ladoA + ladoB > ladoC and ladoB + ladoC > ladoA and ladoA + ladoC > ladoB:
    print('{}É possivel formar o triângulo:{}'.format(cores['roxo'],limpar))
    if ladoA == ladoB == ladoC:
        print('{}Equilátero{}'.format(cores['amarelo'],limpar))
    elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
        print('{}Isósceles{}'.format(cores['amarelo'],limpar))
    else:
        print('{}Escaleno{}'.format(cores['amarelo'],limpar))
else:
    print('{}Não é possivel formar triângulo com esses valores!{}'.format(cores['vermelho'],limpar))
