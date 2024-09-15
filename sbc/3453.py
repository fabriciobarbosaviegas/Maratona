n, k = [int(i) for i in input().split()]

n *= 2

for i in range(n, 0, -1):
    temp = i**2
    if((temp - k)%2 != 0 and i != n):
        print(temp)
        break
