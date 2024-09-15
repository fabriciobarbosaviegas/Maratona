def meio(numeros):

    numeros.sort()

    return numeros[1]



n = []

for i in range(3):
    n.append(int(input()))

print(meio(n))