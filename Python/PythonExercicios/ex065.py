start = True
tot = soma = maior = menor = 0
while start:
    num = int(input('Me diga um Número:'))
    if num == 999:
        print('Você digitou {} Números, a média foi {}, o maior foi {} e o menor foi {}'.format(tot, soma / tot, maior, menor))
        opção = str(input('Você quer continuar, recomeçar ou sair? [C/R/S] : ')).strip().lower()
        if opção == 'r':
            tot = soma = maior = menor = 0
        elif opção == 's':
            start = False
    if num > maior and num != 999:
        maior = num
    elif num < menor:
        menor = num
    if num != 999:
        tot += 1
        soma += num
    if tot == 1:
        maior = menor = num
