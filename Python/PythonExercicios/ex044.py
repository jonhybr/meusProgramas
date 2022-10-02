from datetime import date
from time import sleep
start = True

cores = {'limpar': '\033[m',
         'branco': '\033[1;30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[1;35m',
         'azulclaro': '\033[36m'}
limpar = cores['limpar']

nome = str(input('{}Seu nome:{}'.format(cores['branco'], limpar)))
nasc = int(input('{}Data de nascimento (ano):{}'.format(cores['branco'], limpar)))
idade = date.today().year - nasc

preço = float(input('{}Preço do produto:{}'.format(cores['azul'], limpar)))

print('{}Para comprar você deve escolher uma das opções abaixo:{}'.format(cores['verde'], limpar))
print('==' * 27)
print('{}1{} - {}À vista {}dinheiro/cheque:{} \033[4m10% desconto{}'.format(cores['branco'], limpar, cores['azulclaro'],
                                                                            cores['amarelo'], cores['azulclaro'],
                                                                            limpar))
print('{}2{} - {}À vista no {}catão:{} \033[4m5% desconto{}'.format(cores['branco'], limpar, cores['azulclaro'],
                                                                    cores['amarelo'], cores['azulclaro'], limpar))
print('{}3{} - {}Parcelado 2x no {}cartão:{} \033[4mPreço normal{}'.format(cores['branco'], limpar, cores['azulclaro'],
                                                                           cores['amarelo'], cores['azulclaro'],
                                                                           limpar))
print('{}4{} - {}Parcelado 3x ou mais no {}cartão:{} \033[4m20% juros{}'.format(cores['branco'], limpar,
                                                                                cores['azulclaro'], cores['amarelo'],
                                                                                cores['azulclaro'], limpar))
print('==' * 27)
opção = int(input('{}OPÇÃO:{} '.format(cores['roxo'], limpar)))

if opção == 1:
    preço = preço - (preço * 10 / 100)
elif idade < 18 and opção == 2 or idade < 18 and opção == 3 or idade < 18 and opção == 4:
    print('{}Você não pode usar cartão com menos de 18 anos!{}'.format(cores['vermelho'], limpar))
    preço = 0
elif opção == 2:
    preço = preço - (preço * 5 / 100)
elif opção == 3:
    preço = preço / 2
    par = 2
elif opção == 4:
    par = int(input('{}Quer parcelar em quantas vezes?{}:'.format(cores['azul'],limpar)))
    preço = (preço + (preço * 20 / 100)) / par

if idade >= 18 and opção == 2 or idade >= 18 and opção == 3 or idade >= 18 and opção == 4:
    print('{}PROCESSANDO...{}'.format(cores['vermelho'], limpar))
    sleep(2)

print('{}O preço final vai ser: R${:.2f}'.format(cores['verde'], preço), end=' ')

if opção == 3 and idade > 18 or opção == 4 and idade > 18:
    print('parcelados {} vezes no cartão.'.format(par))
