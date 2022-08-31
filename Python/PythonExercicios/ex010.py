
dolar = 3.27
n1 = float(input('Quanto dinheiro você tem? Me diga e eu direi quantos dólares você pode comprar: R$'))
print('Com R${:.2f} você pode comprar U${:.2f}'.format(n1, n1 / dolar))
