fact = [1,1,2,6,24,120,720,5040,40320,362880]

n = int(input())
c = 0
limite = n

for i in range(10):
    if n - fact[i] < 0:
        limite = i
        break
    else:
        limite = n - fact[i]


fact = fact[:limite]

teste = n

while teste != 0:
    for i in reversed(fact):
        if teste - i >= 0:
            teste -= i
            c += 1
            break

print(c)