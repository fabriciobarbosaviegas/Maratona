molduras = []
AL = input().split()
foto = int(AL[0]) * int(AL[1])

for i in range(int(input())):
    moldura = input().split()
    molduras.append(int(moldura[0])*int(moldura[1]))

min = 99999999999999
c = -1

for i in range(len(molduras)):
    if molduras[i] >= foto and molduras[i] < min:
        min = molduras[i]
        c = i+1

print(c)
