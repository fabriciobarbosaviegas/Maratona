amigos = {'Amigo':[], 'T':[], 'R':[], 'E':[]}

for i in range(int(input())):
    evento = input()
    evento = evento.split()

    if evento[0] == 'R':
        if not evento[1] in amigos['Amigo']:
            amigos['Amigo'].append(evento[1])
            amigos['T'].append(0)
            amigos['R'].append(1)
            amigos['E'].append(0)

            for i in range(len(amigos['Amigo'])-1):
                if amigos['E'][i] == 0:
                    amigos['T'][i] += 1

        else:
            amigos['E'][amigos['Amigo'].index(evento[1])] = 0
            amigos['R'][amigos['Amigo'].index(evento[1])] = 1

            for i in range(len(amigos['Amigo'])):
                if amigos['Amigo'][i] != evento[1] and amigos['E'][i] == 0:
                    amigos['T'][i] += 1
                    

    elif evento[0] == 'E':
        amigos['E'][amigos['Amigo'].index(evento[1])] = 1

        for i in range(len(amigos['Amigo'])):
            if amigos['Amigo'][i] != i and amigos['E'][i] == 0:
                amigos['T'][i] += 1

    elif evento[0] == 'T':
        for i in range(len(amigos['Amigo'])):
            amigos['T'][i] += int(evento[1])

amigosOrdenado = sorted(amigos['Amigo'])

for i in range(len(amigos['Amigo'])):
    print(f"{amigosOrdenado[i]} ", end='')
    
    if amigos['E'][amigos['Amigo'].index(amigosOrdenado[i])] == 0:
        print(-1)

    else:
        print(amigos['T'][amigos['Amigo'].index(amigosOrdenado[i])])