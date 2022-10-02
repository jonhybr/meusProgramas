from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} contando de {passo} em {passo}')
    while True:
        print(inicio, end=' ')
        sleep(0.2)
        if inicio == fim:
            print()
            break
        if inicio >= fim:
            inicio -= passo
        else:
            inicio += passo


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora você escolhe: ')
ini = int(input('Inicio:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)
