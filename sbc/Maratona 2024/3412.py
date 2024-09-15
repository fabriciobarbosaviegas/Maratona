alunos = {}

for i in range(int(input())):
    nome = input()
    alunos[nome] = [float(i) for i in input().split()]
    menorNota = min(alunos[nome])

    total = len(alunos[nome])
    if total < 2:
        alunos[nome] = alunos[nome][0]/2
    elif total > 3 and alunos[nome][3] > menorNota:
        alunos[nome].remove(menorNota)
        alunos[nome] = sum(alunos[nome])/(total-1)
    elif total > 3 and alunos[nome][3] <= menorNota:
        alunos[nome] = sum(alunos[nome][:total-1])/(total-1)
    else:
        alunos[nome] = sum(alunos[nome])/total

for i in alunos:
    print(f'{i}: {round(alunos[i], 1)}')