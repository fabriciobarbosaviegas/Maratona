def maximum_pieces(N, M, intervals):
    # Initialize a DP table
    dp = [0] * (N + 1)

    # Sort the intervals by their end point Ri
    intervals.sort(key=lambda x: x[1])

    # Array to store the last covering interval for each position
    last_covered = [-1] * (N + 1)
    idx = 0

    # Fill last_covered array
    for i in range(1, N):
        while idx < M and intervals[idx][1] <= i:
            idx += 1
        if idx < M and intervals[idx][0] <= i:
            last_covered[i] = idx

    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + 1
        if last_covered[i] != -1:
            dp[i] = min(dp[i], dp[intervals[last_covered[i]][0]] + 1)

    return dp[N]

# Exemplo de uso
N = 7
M = 3
intervals = [(1, 5), (2, 5)]

print(maximum_pieces(N, M, intervals)) 