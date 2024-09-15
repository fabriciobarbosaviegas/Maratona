def ehEspecial(NM, M):
    L = N*M
    N = L // M
        
    for start in range(N):
        count = []
        for i in range(N):
            blocoComeco = (start + i * M) % L
            bloco = NM[blocoComeco:blocoComeco + M] + NM[:max(0, blocoComeco + M - L)]
            preto = sum(bloco)
            count.append(preto)

        if len(count) != len(set(count)):
            return 'N'
    
    return 'S'

N, M = [int(i) for i in input().split()]
NM = [int(i) for i in input()]
print(ehEspecial(NM, M))