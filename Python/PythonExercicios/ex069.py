continuar = True
p18a = homens = m18a = pessoas = pessoa = 0
while continuar:
    pessoa += 1
    print('--'*4, '{}º pessoa'.format(pessoa), '--'*4)
    idade = int(input('Me diga uma idade: '))
    sexo = str(input('É Homem[H] ou Mulher[M]? : ')).upper()
    while sexo not in ('HMhm'):
        sexo = str(input('É Homem[H] ou Mulher[M]? : ')).upper()
    pessoas += 1
    opc = str(input('Que continuar [S/N]? : ')).upper()
    while opc not in ('SsNn'):
        opc = str(input('Que continuar [S/N]? : ')).upper()
    if idade >= 18:
        p18a += 1
    if sexo == 'H':
        homens += 1
    if idade < 20 and sexo == 'M':
        m18a += 1
    if opc == 'N':
        break
print(f'Das {pessoas}, {p18a} pessoas tem mais de 18 anos, {homens} homens foram cadastrados e {m18a} mulheres tem menos de 20 anos.')
