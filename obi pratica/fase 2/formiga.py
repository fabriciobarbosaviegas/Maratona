alcancados = 0

def busca(partida):
    global alcancados

    if not visitados[partida]:
        alcancados += 1
        visitados[partida] = True
        for i in adj[partida]:
            busca(i)

S, T, P = [int(i) for i in input().split()]
altura = [int(i) for i in input().split()]
visitados = [False for i in range(S)]

adj = [[] for i in range(S)]

for i in range(T):
    x, y = [int(j) for j in input().split()]
    x -= 1
    y -= 1

    if altura[x] > altura[y]:
        adj[x].append(y)

    elif altura[x] < altura[y]:
        adj[y].append(x)

print(adj)

busca(P-1)
print(alcancados-1)