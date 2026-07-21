dominios = {}
for _ in range(int(input())):
    email = input().split('@')
    if email[1] not in dominios:
        dominios[email[1]] = []
    dominios[email[1]].append(email[0])

for i in dominios:
    dominios[i] = [x.replace('.','') for x in dominios[i]]

    for x, j in enumerate(dominios[i]):
        if '+' in j:
            dominios[i][x] = j.split('+')[0]

for i in dominios:
    dominios[i] = set(dominios[i])

c = 0

for i in dominios:
    c += len(dominios[i])
print(c)