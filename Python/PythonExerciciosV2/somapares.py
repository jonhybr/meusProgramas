resultado = 0
numeros = [[], []]

for n in range(0, 6):
    num = int(input(f"Digite o {n+1}º número: "))
    if num % 2 == 0:
        resultado += num
        numeros[1].append(num)
    numeros[0].append(num)

print(f"Você digitou os números: {numeros[0]} dos quais {len(numeros[1])} foram pares, que são {numeros[1]} e a soma dos pares é igual a {resultado}")
