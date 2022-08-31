altura = float(input('Qual a sua altura?:'))
peso = float(input('Qual o seu peso?:'))
imc = peso / altura ** 2

if imc < 18.5:
    print('Seu IMC está abaixo de 18.5, você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Seu IMC está entre 18.5 e 25, ou seja, seu IMC é ideal para sua altura e peso atuais.')
elif 25 < imc <= 30:
    print('Seu IMC está entre 25 e 30, você está com sobrepeso.')
elif 30 < imc <= 40:
    print('Seu IMC está entre 30 e 40, você está com obesidade.')
elif imc > 40:
    print('Seu IMC está maior que 40, você está com obesidade mórbida.')
