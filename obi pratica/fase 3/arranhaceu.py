def bombeiro(K):
    T = 0
    
    for i in range(K):
        T += M[i]
    
    return(T)

N, Q = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]
R = []

for i in range(Q):
    E = [int(i) for i in input().split()]

    if E[0] == 0:
        M[E[1]-1] = E[2]
    elif E[0] == 1:
        R.append(bombeiro(E[1]))

for i in R:
    print(i)