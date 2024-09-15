def menor_numero_paradas(N, K, A, B):
    current_tobacco = K
    current_position = 0
    stops = 0
    
    for i in range(N):
        if A[i] > current_tobacco:
            if i == 0:
                return -1
            current_tobacco = B[i-1]  # Fuma todo o tabaco que trouxe até agora
            stops += 1
        
        current_tobacco -= A[i] - current_position
        current_position = A[i]
        
        if current_position >= A[-1]:
            break
    
    if current_position < A[-1]:
        if current_tobacco < A[-1] - current_position:
            return -1
        else:
            current_tobacco = B[-1]
            stops += 1
    
    return stops

N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

print(menor_numero_paradas(N, K, A, B))  # Saída esperada: 2
