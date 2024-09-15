a, b, c, d = [int(i) for i in input().split()]

if (a == b or c == d or c%a != 0): print(-1)
else:
    n = -1
    for i in range(0, c, a):
        if i%a==0 and i%b!=0 and c%i==0 and d%i!=0:
            n = i
            break
    print(n)