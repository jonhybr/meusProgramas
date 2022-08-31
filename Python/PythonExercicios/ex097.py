def escreva(msg):
    print('~' * (len(msg) + 6))
    print(f'   {msg}')
    print('~' * (len(msg) + 6))


while True:
    palavra = str(input('Palavra: '))
    escreva(palavra)
