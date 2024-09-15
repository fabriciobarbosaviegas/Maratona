N = int(input())
X = [int(i) for i in input().split()]

c = 0
r = 0

for i in X:
    if i >= 50 and i < 85:
        r += 1
    elif i < 50:
        c += 1

print(f"{c} {r}")