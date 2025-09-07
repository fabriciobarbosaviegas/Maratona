#include <bits/stdc++.h>
using namespace std;

// Crivo de Eratóstenes para gerar primos até 46340
vector<int> sieve(int limit = 46340) {
    vector<bool> is_prime(limit + 1, true);
    vector<int> primes;
    for (int p = 2; p <= limit; p++) {
        if (is_prime[p]) {
            primes.push_back(p);
            if ((long long)p * p <= limit) {
                for (int multiple = p * p; multiple <= limit; multiple += p) {
                    is_prime[multiple] = false;
                }
            }
        }
    }
    return primes;
}

// Função totiente de Euler
long long totient(long long n, const vector<int>& primes) {
    long long res = n;
    long long temp = n;
    for (int p : primes) {
        if ((long long)p * p > temp) break;
        if (temp % p == 0) {
            while (temp % p == 0) temp /= p;
            res -= res / p;
        }
    }
    if (temp > 1) res -= res / temp;
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> primes = sieve();

    long long N;
    while (cin >> N) {
        cout << totient(N, primes) / 2 << "\n";
    }
    return 0;
}