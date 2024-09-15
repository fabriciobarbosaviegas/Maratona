[N, C, M] = input().split()
X = input().split()
Y = input().split()

carimbadas = 0

for i in Y:
    if i in X:
        carimbadas += 1
        X[X.index(i)] = 0

print(int(C) - carimbadas)