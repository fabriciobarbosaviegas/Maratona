def direcoes(direcao, coluna, linha):
    if direcao == 'O':
        for i in range(linha-1, -1, -1):
            if tabuleiro[coluna][i] != 2:
                tabuleiro[coluna][i] = 2
            else:
                break
    elif direcao == 'L':
        print(list(range(linha+1, M-1, -1)))
        for i in range(linha+1, M-1, -1):
            if tabuleiro[coluna][i] != 2:
                tabuleiro[coluna][i] = 2
            else:
                break
    elif direcao == 'N':
        for i in range(0, N-1):
            if tabuleiro[i][linha] != 2:
                tabuleiro[i][linha] = 2
            else:
                break
    elif direcao == 'S':
        for i in range(N-1, 0, -1):
            if tabuleiro[i-1][linha] != 2:
                tabuleiro[i-1][linha] = 2
            else:
                break
            
N, M, K = [int(i) for i in input().split()]
camera = []

for i in range(K):
    camera.append(input().split())
    
tabuleiro = [[0 for i in range(N)]]

for i in range(M-1):
    tabuleiro.append([0 for i in range(N)])

for i in camera:
    tabuleiro[int(i[1])-1][int(i[0])-1] = 2
    direcoes(i[2], int(i[1])-1, int(i[0])-1)
 
for i in tabuleiro:
    print(i)