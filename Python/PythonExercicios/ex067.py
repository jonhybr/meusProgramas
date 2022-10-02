while True:
    num = int(input('\033[34mMe diga um Número: \033[32m(\033[4:32mDigite um número negativo para sair\033[m\033[32m)\033[m '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c:2}')
