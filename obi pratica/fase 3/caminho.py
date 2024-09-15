pista = []
trechoEscuro = []
N = int(input())

for i in range(N):
    pista.append(int(input()))

c = 0

for i in range(N):
    if pista[i] + pista[i+1 if i < N-1 else 0] < 1000:
        c += 1
    
    else:
        trechoEscuro.append(c)
        c = 0

trechoEscuro.append(c)

trechoEscuro.sort(reverse=True)

print(trechoEscuro[0])