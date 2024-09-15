n = int(input())
h = [int(i) for i in input().split()]

c = 0 if h[n-1] > h[n-2] else 1
pos = h[0]

while 
    for i in range(n-1):
        if h[i] > h[i+1]:
            c += 1

print(c)