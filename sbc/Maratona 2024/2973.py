N, C, T = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]

left = 1
right = sum(P) // T + 1

while left < right:
    mid = (left + right) // 2
    max_pipocas = mid * T
    competidores = 1
    pipocas_atual = 0
    
    for pipoca in P:
        if pipoca > max_pipocas:
            left = mid + 1
            break
        if pipocas_atual + pipoca > max_pipocas:
            competidores += 1
            pipocas_atual = pipoca
            if competidores > C:
                left = mid + 1
                break
        else:
            pipocas_atual += pipoca
    else:
        right = mid

print(left)