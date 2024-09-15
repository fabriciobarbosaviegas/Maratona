n = str(input()).split()
mapas = []

for i in range(int(n[0])):
    mapas.append(str(input()))

print(mapas)

for i in range(int(n[0])):
    for j in range(int(n[0])):
        if int(mapas[i][j]) <= int(n[1]):
            mapas[i] = mapas[i].replace(mapas[i][j], '*', 1)

            for k in range(i+1, int(n[0])):
                print(mapas[k])
                if int(mapas[k][j]) <= int(n[1]):
                    mapas[k] = mapas[k].replace(mapas[k][j], '*', 1)

        else:
            break

print(mapas)