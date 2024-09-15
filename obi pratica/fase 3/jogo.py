L, C = [int(i) for i in input().split()]
P = int(input())

coop = []
coob = []

for i in range(P):
    coop.append([int(i) for i in input().split()])

print(f'L: {L} | C: {C} | P: {P} | cooprdenadas: {coop}')

#tabuleiro = [[0 for i in range(C)] for j in range(L)]

'''for i in coop:
    tabuleiro[i[0]-1][i[1]-1] = 1
'''
total = P*4
for i in range(P):
    if not [coop[i][0]-1, coop[i][1]-1] in coob and not [coop[i][0]-1, (coop[i][1]-1)+2] in coob:
        if not [coop[i+1][0]-1, (coop[i][1]-1)+2]
        coob.append([coop[i][0]-1, coop[i][1]+1])

print(coob)