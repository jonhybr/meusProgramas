exp = str(input('Digite uma espressão numérica: '))
aberto = fechado = 0
for c in exp:
    if c == '(':
        aberto += 1
    elif c == ')':
        fechado += 1
if aberto == fechado:
    print('A operação é valida.')
else:
    print('A operação é invalida.')
