sal = float(input('Parabéns você foi promovido e seu salário vai aumentar em 15%, me diga seu salário atual: R$'))
promoção = sal + (sal * 15 / 100)
print('Uau, seu salário era R${:.2f} e aumentou para R${:.2f}'.format(sal,promoção))
