def solve():
    N, M = map(int, input().split())
    K, L = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(input()))

    # Initialize the attacks matrix with zeros
    attacks = [[0] * M for _ in range(N)]

    # Iterate over each empty cell in the board
    for i in range(N):
        for j in range(M):
            if board[i][j] == '.':
                # Iterate over all possible moves of the Mula Sem Cabeça
                for k in range(-K, K+1):
                    for l in range(-L, L+1):
                        # Check if the move is valid and if it attacks a black pawn
                        if 0 <= i+k < N and 0 <= j+l < M and board[i+k][j+l] == '*':
                            # Add 1 to the number of attacks of the current cell
                            attacks[i][j] += 1

    # Find the cell with the maximum number of attacks
    max_attacks = 0
    best_position = (-1, -1)
    for i in range(N):
        for j in range(M):
            if attacks[i][j] > max_attacks:
                max_attacks = attacks[i][j]
                best_position = (i, j)

    # Print the result
    print(*best_position)

solve()