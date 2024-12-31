res = []

while True:
    N, M = [int(i) for i in input().split()]

    if N + M == 0:
        break

    pedido = []
    estoque = []

    for i in range(N):
        pedido.append([int(i) for i in input().split()])
        pedido[i] = pedido[i][0]*pedido[i][1]*pedido[i][2]
    
    for i in range(M):
        estoque.append([int(i) for i in input().split()])
        estoque[i] = estoque[i][0]*estoque[i][1]*estoque[i][2]
    
    for i in pedido:
        sobra = 0
        if i in estoque:
            sobra += 0

for i in res:
    print(i)