res = []
for i in range(int(input())):
    tempo, turno = [int(i[0] if 'T' in i else i) for i in input().split()]
    
    if turno == 1 and tempo <= 45:
        res.append(tempo)
    elif turno == 1 and tempo >= 45:
        res.append(f'45+{tempo-45}')
    if turno == 2 and tempo <= 45:
        res.append(tempo+45)
    elif turno == 2 and tempo >= 45:
        res.append(f'90+{tempo-45}')

[print(i) for i in res]