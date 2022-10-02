from time import sleep
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m',
         'azulclaro': '\033[36m',
         'azulclaroN': '\033[1;36m',
         'branco': '\033[1;30m',
         'roxo': '\033[1;35m'
         }
limpar = cores['limpa']

nota1 = float(input('{}Me diga sua {}Primeira {}Nota:{} '.format(cores['azulclaro'],cores['azulclaroN'],cores['branco'],limpar)))
nota2 = float(input('{}Me diga sua {}Segunda {}Nota:{} '.format(cores['azulclaro'],cores['azulclaroN'],cores['branco'],limpar)))
resultado = (nota1 + nota2) / 2
print('-=-'*9)
print('{}CARREGANDO MÉDIA...{}'.format(cores['roxo'],limpar))
print('-=-'*9)
sleep(4)

if resultado < 5:
    print('{}Sua media é {:.1f}\nVocê foi reprovado!{}'.format(cores['vermelho'],resultado,limpar))
elif 5 <= resultado < 7:
    print('{}Sua media é {:.1f}\nVocê vai precisar fazer recuperação!{}'.format(cores['verde'],resultado,limpar))
elif resultado >= 7:
    print('{}Sua media é {:.1f}\nParabéns você foi aprovado!{}'.format(cores['amarelo'],resultado,limpar))

