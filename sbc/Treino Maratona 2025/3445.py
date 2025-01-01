res = []
N, H, W = [int(i) for i in input().split()]

for _ in range(N):
    aux = []
    dia = input().split()

    if dia[0] == 'Y':
        if H > 0:
            H -= 1  
            W += 1  
        aux.append('Y')

    elif dia[0] == 'N':  
        if W == 0 and H > 0:  
            H -= 1
            W += 1
            aux.append('Y')
        else:
            aux.append('N')

    if dia[1] == 'Y':
        if W > 0:
            W -= 1 
            H += 1 
        aux.append('Y')
    
    elif dia[1] == 'N': 
        if H == 0 and W > 0:  
            W -= 1
            H += 1
            aux.append('Y')
        else:
            aux.append('N')

    res.append(aux)

for i in res:
    print(f'{i[0]} {i[1]}')
