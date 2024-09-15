numeros = []
soma = 0

for i in range(int(input())):
    numero = int(input())

    if numero == 0:
        numeros.pop(len(numeros)-1)

    else:
        numeros.append(numero)

for i in numeros:
    soma += i

print(soma)