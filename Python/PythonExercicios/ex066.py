soma = tot = 0
while True:
    num = int(input('Me diga um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    tot += 1
print(f'Você digitou {tot} Números, e a soma entre eles é {soma}.')