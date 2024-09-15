rotas = []
caminhosPagos = 0

for i in range(int(input())-1):
    rota = input().split()
    rotas.append(rota)

if len(rotas) > 1:

    for i in range(0, len(rotas), 1):

        if i+1 < len(rotas):
            if rotas[i][2] == rotas[i+1][2]:
                caminhosPagos += 1
        
        else:
            if rotas[i][2] == rotas[i-1][2]:
                caminhosPagos += 1

else:

    caminhosPagos = 2

print(caminhosPagos)