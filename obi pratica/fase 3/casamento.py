def igualarCasas():
    while len(A) < len(B):
        A.insert(0, 0)

    while len(B) < len(A):
        B.insert(0, 0)    

A = [int(i) for i in input()]
B = [int(i) for i in input()]

NA = []
NB = []

igualarCasas()

for i in range(len(A)):
    if A[i] > B[i]:
        NA.append(A[i])
    elif B[i] > A[i]:
        NB.append(B[i])
    else:
        NA.append(A[i])
        NB.append(B[i])

NA = int(''.join([str(i) for i in NA])) if NA != [] else -1
NB = int(''.join([str(i) for i in NB])) if NB != [] else -1

if NA < NB:
    print(f'{NA} {NB}')

else:
    print(f'{NB} {NA}')