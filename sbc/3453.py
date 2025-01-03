n, k = [int(i) for i in input().split()]
limite = 2 * n
mod = limite + 1

x = limite**2

while abs(x - k) % mod != 0:
    limite -= 1  
    x = limite**2  

print(x)
