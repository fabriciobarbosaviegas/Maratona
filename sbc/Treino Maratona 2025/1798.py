N, T = [int(i) for i in input().split()]

C = []
V = []

for _ in range(N):
    CV = [int(i) for i in input().split()]
    C.append(CV[0])
    V.append(CV[1])

dp = [0] * (T+1)

for j in range(1, T + 1):
    for i in range(N):
        if C[i] <= j:
            dp[j] = max(dp[j], dp[j - C[i]] + V[i])
print(dp[T])