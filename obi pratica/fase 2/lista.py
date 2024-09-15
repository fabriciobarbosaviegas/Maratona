def contracao(lista):
    if len(lista) % 2 == 0:
        meio = round(len(lista)/2)+1
    else:
        meio = round(len(lista)/2)
    print(meio)
    comparadores = lista[:meio]

    for i in lista[meio:]:
        if not i in comparadores:
            soma = lista[meio] + (lista[meio+1] if meio != len(lista)-1 else meio-1)
            del lista[meio]
            lista[meio] = soma
            break
        
    return lista

N = int(input())
L = [int(i) for i in input().split()]

c = 0

while L != list(reversed(L)):
    L = contracao(L)
    print(L)
    L = list(reversed(L))
    c += 1

else:
    print(c)