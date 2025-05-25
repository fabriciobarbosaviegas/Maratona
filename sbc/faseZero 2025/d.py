def calcular_taxa_decoerencia():
    n = int(input())
    s_isolado = input()
    t_normal = input()

    qubits_superposicao_isolado = 0
    qubits_colapsados = 0

    for i in range(n):
        if s_isolado[i] == '*':
            qubits_superposicao_isolado += 1
            if t_normal[i] != '*':  
                qubits_colapsados += 1
    
    if qubits_superposicao_isolado == 0:
        taxa = 0.0
    else:
        taxa = qubits_colapsados / qubits_superposicao_isolado

    print(f"{taxa:.2f}")

if __name__ == "__main__":
    calcular_taxa_decoerencia()