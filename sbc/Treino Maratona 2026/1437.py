res = []
direcoes = {'D':1, 'E':-1}
rosaDosVentos = ['N', 'L', 'S', 'O']

while True:
    soldado = 0

    if input() == '0':
        break

    for i in input():
        soldado += direcoes[i]
        soldado %= 4

    res.append(rosaDosVentos[soldado])

[print(i) for i in res]