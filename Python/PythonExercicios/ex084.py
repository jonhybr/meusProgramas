pessoas = []
pesados = []
leves = []
maiorpeso = menorpeso = count = 0
while True:
    count += 1
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    if peso == maiorpeso:
        pesados.append(nome)
    if peso == menorpeso:
        leves.append(nome)
    if count == 1:
        maiorpeso = menorpeso = peso
        pesados.append(nome)
        leves.append(nome)
    if peso > maiorpeso:
        maiorpeso = peso
        pesados.clear()
        pesados.append(nome)
    if peso < menorpeso:
        menorpeso = peso
        leves.clear()
        leves.append(nome)
    opc = str(input('Quer continuar? [S/N]: ')).strip().lower()
    while opc not in 'sn':
        opc = str(input('Quer continuar? [S/N]: ')).strip().lower()
    if opc == 'n':
        break
print('=-'*18)
print(f'Você cadastrou {count} pessoas.\nO maior peso foi {maiorpeso} que foram:')
for c in pesados:
    print(f'|{c}|', end='')
print(f'\nO menor peso foi {menorpeso} que foram:')
for c in leves:
    print(f'|{c}|', end='')
