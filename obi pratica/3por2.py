import math

def criaConjuntos(numeros):
    conjuntos = []
    c = 0

    for i in range(math.ceil(len(numeros)/3)):
        
        conjunto = []
        
        counter = 0
        
        while counter < 3:

            if (counter + c) >= len(numeros):
                break

            else:
                conjunto.append(numeros[counter + c])

                counter += 1

        conjuntos.append(conjunto)
        
        c += 3
    
    return conjuntos


def pegaOsValoresDaSoma(conjunto):
    
    valoresDaSoma = []

    for i in range(len(conjunto)):
        valoresDaSoma.append(conjunto[i][len(conjunto[i]) - 1])

        if len(conjunto[i]) > 1:
            valoresDaSoma.append(conjunto[i][len(conjunto[i]) - 2])

    return valoresDaSoma



def somaArray(valoresDaSoma):
    soma = 0

    for i in valoresDaSoma:
        soma += i

    return soma



p = []

for i in range(int(input())):
    p.append(int(input()))

p.sort()

conjuntos = criaConjuntos(p)

valoresDaSoma = pegaOsValoresDaSoma(conjuntos)

print(somaArray(valoresDaSoma))