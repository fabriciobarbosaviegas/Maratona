def menorTempo(rotas, V, T, partida, chegada):
    minT = 999999999999999999
    minR = []
    rV = 0

    for i in rotas:
        if partida in i[0:2] and i[2] < minT and i[3] <= V:
            minT = i[2]
            rV = i[3]
            minR = i

    if minR != []:    
        V -= rV
        T += minT
        partida = minR[0] if minR[0] != partida else minR[1]

        if V < 0:
            return print(-1)

        elif partida == chegada:
            return print(T)

        else:
            menorTempo(rotas, V, T, partida, chegada)
    
    else:
        return print(-1)

V, N, M = [int(i) for i in input().split()]
rotas = []
T = 0

for i in range(M):
    rotas.append([int(i) for i in input().split()])

X, Y = [int(i) for i in input().split()]

menorTempo(rotas, V, T, X, Y)