n = int(input())
b = [int(i) for i in input().split()]

flechas = {}
c = 0

for altura in b:
    if flechas.get(altura, 0) > 0:
        flechas[altura] -= 1
        flechas[altura - 1] = flechas.get(altura - 1, 0) + 1
    else:
        c += 1 
        flechas[altura - 1] = flechas.get(altura - 1, 0) + 1

print(c)
