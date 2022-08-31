tot = num = somatotal = 0
while num != 999:
    num = int(input('Me diga um Número [999 para parar]: '))
    if num != 999:
        tot += 1
        somatotal += num
print('Você digitou {} Números e a soma entre eles foi {}'.format(tot, somatotal))
