valor = float(input('Atenção estamos com 5% de desconto em todos os produtos me diga um preço que te digo com desconto: R$'))
dis = valor * 5 / 100
print('O produto que custa R${}, agora está custando R${:.2f} com a promoção aproveite!'.format(valor, valor - dis))