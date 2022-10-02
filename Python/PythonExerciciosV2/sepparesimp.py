numeros = [[], [], []]

while True:
    num = int(input("Digite um valor: "))
    numeros[0].append(num)
    if num % 2 == 0:
        numeros[2].append(num)
    else:
        numeros[1].append(num)
    opc = str(input("Quer continuar? [S/N]: ")).lower()
    if opc == "n":
        break

print(f"Foram digitados {len(numeros[0])} números.\nOs números digitos foram {numeros[0]}\nOs números pares são {numeros[2]}\nOs números ímpares são {numeros[1]}")
