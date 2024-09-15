amigos = {}
aguardando = []


for i in range(int(input())):
    evento, valor = [i for i in input().split()]
    tempo = 1

    if evento == 'T':
        tempo = int(valor)
    if evento == 'E':
        aguardando.remove(valor)
    
    for i in aguardando:
        amigos[i] += tempo
        
    if evento == 'R' and not valor in amigos:
        aguardando.append(valor)
        amigos[valor] = 0

    print(amigos)
    print(aguardando)

for i in sorted(amigos.keys()):
    if(i in aguardando):
        print(f'{i} -1')
    else:
        print(f'{i} {amigos[i]}') 