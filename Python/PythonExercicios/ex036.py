cores = {'limpa': '\033[m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m',
         'azulclaro' : '\033[1;36m',
         'cinza': '\033[1;37m',
         'vermelho': '\033[1;31m',
         'branco': '\033[1;30m',
         'azul': '\033[1;34m'}

valcas = float(input('A {}Casa{} que você quer comprar custa? : {}R${}'.format(cores['amarelo'], cores['limpa'], cores['verde'],cores['limpa'])))
sal = float(input('Para o {}Empréstimo{} ser aprovado precisamos saber qual seu {}Salário{} atual: {}R${}'.format(cores['azulclaro'],cores['limpa'],cores['branco'],cores['limpa'],cores['verde'],cores['limpa'])))
par = int(input('E em quantas anos você quer {}Parcelar{}:'.format(cores['vermelho'],cores['limpa'])))
res = valcas / (par * 12)

if valcas / (par * 12) < sal * 30 / 100:
    print('Parece que podemos fazer o {}Empréstimo{}!'.format(cores['azulclaro'],cores['limpa']))
    print('Cada mês você será cobrado em {}R${}{}{:.2f}{}'.format(cores['verde'],cores['limpa'],cores['branco'],res,cores['limpa']))
else:
    print('Sinto muito não podemos fazer o {}Empréstimo{}, pois o custo excede 30% de seu salário'.format(cores['azulclaro'],cores['limpa']))
