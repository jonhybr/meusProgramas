prim = int(input('O primeiro termo é: '))
razão = int(input('A razão é: '))
decimo = 0
fim = 10
while decimo < fim:
    print('{} ->'.format(prim), end=' ')
    prim += razão
    decimo += 1
    if decimo == fim:
        print('Acabou!')
        opção = str(input('Você quer adicionar mais termos? [S/N] : ')).lower().strip()
        if opção == 's':
            resposta = int(input('Quantos? : '))
            fim += resposta
            if resposta == 0:
                decimo = fim
        else:
            acabo = str(input('Continuar? [S/N] : ')).lower().strip()
            if acabo == 's':
                prim = int(input('O primeiro termo é: '))
                razão = int(input('A razão é: '))
                decimo = 0
                fim = 10
print('Foram mostrados {} termos'.format(decimo))
