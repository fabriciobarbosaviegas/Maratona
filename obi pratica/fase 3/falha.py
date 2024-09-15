N = int(input())
S = []

for i in range(N):
    S.append(input())

c = 0

for i in S:
    for j in S:
        if i in j:
            c += 1
    c -= 1

print(c)