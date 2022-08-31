start = True
while start:
    frase = str(input('Me diga uma frase palíndromo: ')).replace(' ', '').upper().strip()
    contrario = ''
    for c in range(len(frase) - 1, -1, -1):
        contrario += frase[c]
    print('{} - {}'.format(frase,contrario))
    if contrario == frase:
        print('A frase é Palíndromo')
    else:
        print('A frase não é Palíndromo')
