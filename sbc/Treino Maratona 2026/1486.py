while True:
    P, N, C = [int(i) for i in input().split()]

    if P == N == C == 0:
        break

    count = 0
    tabela = []
    for _ in range(N):
        tabela.append([int(i) for i in input().split()])  

    tabela.append([0]*P)

    varetas = [0]*P

    for i in tabela:
        for j in range(P):
            if i[j] == 1:
                varetas[j] += 1
            else:
                if varetas[j] >= C:
                    count += 1
                varetas[j] = 0
    print(count)