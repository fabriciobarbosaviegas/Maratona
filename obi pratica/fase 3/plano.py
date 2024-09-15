N = list(range(1, int(input())+1))
M = int(input())
V = []

for i in range(M):
    V.append(int(input()))

c = 0
gameOver = False

for i in V:
    for j in range(i, 0, -1):
        if N[j-1] != 0:
            N[j-1] = 0
            c += 1
            break
        elif j-1 == 0:
            gameOver = True

    if gameOver:
        break

print(c)    