N, M = [int(i) for i in input().split()]
c = 0

for i in range(N):
    if 0 in [int(i) for i in input().split()]:
        continue
    else:
        c += 1

print(c)