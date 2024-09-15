res = []
while True:
    N, M = [int(i) for i in input().split()]

    if(N == 0 and M == 0):
        break
    
    cliente = []

    for i in range(N):
        caixa = [int(i) for i in input().split()]
        cliente.append(caixa[0]*caixa[1]*caixa[2])
    
    for i in range(M):
        caixa = [int(i) for i in input().split()]
        if caixa in cliente:
            res.append(0)
        else:
            res.append("impossible")

[print(i) for i in res]