pessoas = []
po = 0
while True:
    nome = str(input('Nome: '))
    media: float = float(input('Nota: '))
    media2 = float(input('Nota: '))
    tot = (media + media2) / 2
    pessoas.append([nome, media, media2, tot])
    opc = str(input('Quer continuar? [s/n]: ')).lower().strip()
    if opc == 'n':
        print('=-'*15)
        print(f'{"No.":<4} {"Nome":<10}{"Média":>11}')
        for c in range(0, len(pessoas)):
            if c <= len(pessoas):
                print(f'{po+1:<4} {pessoas[c][0]:<10} {pessoas[c][3]:>10}')
                po += 1
        print('=-' * 15)
        opc2 = int(input('Escolha para ver a nota (0 para cancelar): '))
        while opc2 != 0:
            print(f'As Notas de {pessoas[opc2-1][0]} são: {pessoas[opc2-1][1]} {pessoas[opc2-1][2]}')
            opc2 = int(input('Escolha para ver a nota (0 para sair): '))
        break
