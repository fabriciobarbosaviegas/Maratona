S = int(input())
Q = sorted([int(i) for i in input().split()])
N = sorted([int(i) for i in input().split()])

w = 0

i, j = 0, 0
while i < S and j < S:
    if N[j] > Q[i]:
        w += 1
        i += 1
    j += 1

print(w)