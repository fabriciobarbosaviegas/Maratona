#include <stdio.h>
#include <math.h>
#define MOD 998244353

long long mul_inv(long long a) {
    return pow(a, MOD - 2) % MOD;
}

long long prob(long long T, long long K) {
    long long num = pow(T, K - 1) % MOD;
    for (long long p = 2; p <= K; p++) {
        num = (num * (p * T - 1) % MOD * mul_inv(p)) % MOD;
    }
    long long den = pow(2, 1000000) % MOD;
    long long prob = (num * mul_inv(den)) % MOD;
    return (prob * mul_inv(den - 1)) % MOD;
}

int main() {
    long long T, K;
    scanf("%lld %lld", &T, &K);
    printf("%lld\n", prob(T, K));
    return 0;
}
