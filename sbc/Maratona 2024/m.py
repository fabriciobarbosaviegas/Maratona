def matinta_pereira(N, M, D):
    # Calcula o número de casas (nós)
    casas = 2 * D + 1
    
    estradas = casas - 1
    
    return casas, estradas

print(matinta_pereira(5, 5, 2))  # (3, 3)
print(matinta_pereira(3, 2, 1))  # (1, 1)