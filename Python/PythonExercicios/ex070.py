count = custoprodmb = tot = prodcaro = 0
nprodmb = ''
print('-'*30, '\n', '{:^30}'.format('Mercadão show'),)
print('-'*30)
while True:
    nprod = str(input('Qual o nome do produto: '))
    custoprod = float(input('O preço do produto é: R$'))
    count += 1
    tot += custoprod
    if count == 1 or custoprod < custoprodmb:
        custoprodmb = custoprod
        nprodmb = nprod
    if custoprod > 1000:
        prodcaro += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] : ')).upper()
    if continuar == 'N':
        break
print('--'*3, 'Acabou a compra', '--'*3)
print(f'O total foi R${tot:.2f}\n{prodcaro} produto(s) mais de 1000 reais.\nO produtos mais barato foi {nprodmb}, custando R${custoprodmb:.2f}')
