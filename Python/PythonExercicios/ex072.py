numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',\
          'treza', 'quatorze', 'quinze', 'dezesseis', 'dezenove', 'vinte'
num = 0
opc = ''
while True:
    num = int(input('Me diga um Número entre 0 até 20: '))
    if 0 > num or num > 20:
        print('Não entendi sua resposta.', end='')
    if 20 > num > 0:
        print(f'O numero {num} por extenso é', numeros[num])
        opc = str(input('Quer continuar? [S/N] : ')).upper().strip()
        while opc not in 'SN':
            opc = str(input('Não entendi sua resposta. Quer continuar? [S/N] : ')).upper().strip()
        if opc == 'N':
            break
