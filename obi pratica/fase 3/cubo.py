A = int(input())
B = int(input())

c = 0

intervalo = [i for i in range(A, B+1)]

for i in intervalo:
    if round(i**(1/3), 2)%1 == 0 and round(i**(1/2), 2)%1 == 0:
        c += 1

print(c)