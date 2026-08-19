N, X = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]

lm = len(m)
mm = 1
ma = 1

for i in range(lm - 1):
    if m[i+1] - m[i] <= X:
        mm += 1
    else:
        if mm > ma:
            ma = mm
        mm = 1

if mm > ma:
    ma = mm
print(ma)