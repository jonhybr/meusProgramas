from time import sleep
cores = {'vermelho': '\033[1;31m',
         'limpar': '\033[m',
         'verde': '\033[32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;36m',
         'branco': '\033[1;30m'}
limpar = cores['limpar']


print('[', '-'*20, ']')
num1 = int(input('{}Primeiro número:{} '.format(cores['amarelo'],limpar)))
num2 = int(input('{}Segundo número:{} '.format(cores['amarelo'],limpar)))
print('[','-'*20,']')

print('{}PROCESSANDO...{}'.format(cores['vermelho'],limpar))
sleep(1)
if num1 > num2:
    print('{}O primeiro número {}({}{}{}){} é maior!{}'.format(cores['azul'],cores['branco'],cores['verde'],num1,cores['branco'],cores['azul'],limpar))
elif num2 > num1:
    print('{}O segundo número {}({}{}{}){} é maior!{}'.format(cores['azul'],cores['branco'],cores['verde'],num2,cores['branco'],cores['azul'],limpar))
elif num1 == num2:
    print('{}Os números {}({}{}{} {}e {}{}{}{}){}{} tem a mesma quantidade!{}'.format(cores['azul'],cores['branco'],cores['verde'],num1,limpar,cores['branco'],cores['verde'],num2,limpar,cores['branco'],limpar,cores['azul'],limpar))

