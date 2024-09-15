numeros = []

for i in range(int(input())):
    numero = int(input())

    if numero != 0:
        numeros.append(numero)
    else:
        numeros.pop()

if len(numeros) == 0:
    print(0)
else:
    print(sum(numeros))