output = []

while True:
    try:
        botas = {}
        for i in range(int(input())):
            n, p = input().split()
            if not n in botas:
                botas[n] = []
            botas[n].append(p)

        pares = 0

        for i in botas:
            d = botas[i].count("D")
            e = botas[i].count("E")
            if d != 0 or e != 0:
                if d - e == 0:
                    pares += d
                else:
                    pares += d if d < e else e

        output.append(pares)
        pass
    except EOFError:
        [print(i) for i in output]
        break
