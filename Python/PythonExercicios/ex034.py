salario = float(input('Você ganhou uma promoção me diga seu salario atual: R$'))
if salario > 1250:
    promoção = salario * 10 / 100
if salario <= 1250 :
    promoção = salario * 15 / 100

print('Seu antigo salário era R${} , agora seu salário será R${} , Parabéns!'.format(salario,salario+promoção))
