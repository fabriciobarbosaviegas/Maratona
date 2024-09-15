MOD = 998244353

def mul_inv(a):
    return pow(a, MOD - 2, MOD)

def prob(T, K):
    num = den = pow(2, 1000000, MOD)
    for i in range(1, 1 << K):
        p = cnt = 1
        for j in range(K):
            if i & (1 << j):
                p = (p * (j + 1)) % MOD
                cnt += 1
        if cnt % 2 == K % 2:
            num = (num + den // p) % MOD
        else:
            num = (num - den // p) % MOD
    num = (num * pow(T, K - 1, MOD)) % MOD
    prob = (num * mul_inv(den)) % MOD
    return (prob * mul_inv(den - 1)) % MOD

T, K = map(int, input().split())
print(prob(T, K))
