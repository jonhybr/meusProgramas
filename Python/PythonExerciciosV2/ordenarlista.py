numeros = []
pos = 0
for n in range(0, 5):
    num = int(input("Digite um valor: "))
    if len(numeros) > 0:
        for item in numeros:
            if num <= item:
                pos = numeros.index(item)
                numeros.insert(pos, num)
                break
            elif num >= item:
                pos = numeros.index(item) + 1
                numeros.insert(pos, num)
                break
    else:
        numeros.append(num)

    print(numeros)