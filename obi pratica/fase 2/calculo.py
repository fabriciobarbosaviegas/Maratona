def somaDigitos(n):
    soma = 0
    for i in str(n):
        soma += int(i)

    return soma

S = int(input())
A = int(input())
B = int(input())

c = 0

for i in range(A, B+1):
    if somaDigitos(i) == S:
        c += 1

print(c)