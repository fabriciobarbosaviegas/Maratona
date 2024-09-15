def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

    return fact

n = [int(i) for i in input().split()]

sum = 0

for i in n[1:]:
    sum += factorial(i)

print(sum, end='')