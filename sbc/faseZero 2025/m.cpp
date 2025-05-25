#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

const int MOD = 998244353;
const int MAX_VAL = 100005;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int mu[MAX_VAL];
std::vector<int> primes;
int lp[MAX_VAL];
std::vector<int> divs[MAX_VAL];
long long pow2[MAX_VAL];

long long a[MAX_VAL];
long long cnt_multiples[MAX_VAL];
long long f_val[MAX_VAL]; 
long long count_gcd[MAX_VAL];

int N_global;

void sieve() {
    std::fill(lp, lp + MAX_VAL, 0);
    mu[1] = 1;
    for (int i = 2; i < MAX_VAL; ++i) {
        if (lp[i] == 0) {
            lp[i] = i;
            primes.push_back(i);
            mu[i] = -1;
        }
        for (int p : primes) {
            if (p > lp[i] || i * p >= MAX_VAL) break;
            lp[i * p] = p;
            if (p == lp[i]) mu[i * p] = 0;
            else mu[i * p] = -mu[i];
        }
    }

    for (int i = 1; i < MAX_VAL; ++i) {
        for (int j = i; j < MAX_VAL; j += i) {
            divs[j].push_back(i);
        }
    }
}

void precompute_pow2(int max_n_val) {
    pow2[0] = 1;
    for (int i = 1; i <= max_n_val; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
}

void calculate_initial_counts() {
    std::fill(cnt_multiples, cnt_multiples + MAX_VAL, 0);
    std::vector<int> freq_A(MAX_VAL, 0);
    for (int i = 0; i < N_global; ++i) {
        freq_A[a[i]]++;
    }

    for (int d = 1; d < MAX_VAL; ++d) {
        for (int m = d; m < MAX_VAL; m += d) {
            cnt_multiples[d] += freq_A[m];
        }
    }

    for (int g = 1; g < MAX_VAL; ++g) {
        f_val[g] = (pow2[cnt_multiples[g]] - 1 + MOD) % MOD;
    }

    std::fill(count_gcd, count_gcd + MAX_VAL, 0);
    for (int x = 1; x < MAX_VAL; ++x) {
        for (int m = 1; x * m < MAX_VAL; ++m) {
            long long term = (mu[m] * f_val[x * m]) % MOD;
            count_gcd[x] = (count_gcd[x] + term + MOD) % MOD;
        }
    }
}

void update_value(int val, int delta) {
    for (int d : divs[val]) {
        long long k_before_change = cnt_multiples[d];
        cnt_multiples[d] += delta;
        long long k_after_change = cnt_multiples[d];

        long long f_term_old = (pow2[k_before_change] - 1 + MOD) % MOD;
        long long f_term_new = (pow2[k_after_change] - 1 + MOD) % MOD;
        
        f_val[d] = f_term_new; 
        
        long long delta_f_d = (f_term_new - f_term_old + MOD) % MOD;

        if (delta_f_d != 0) {
            for (int x : divs[d]) {
                long long term_change = (mu[d / x] * delta_f_d) % MOD;
                count_gcd[x] = (count_gcd[x] + term_change + MOD) % MOD;
            }
        }
    }
}


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    sieve();
    
    int n_val;
    std::cin >> n_val;
    N_global = n_val;

    precompute_pow2(N_global);

    for (int i = 0; i < N_global; ++i) {
        std::cin >> a[i];
    }

    calculate_initial_counts();

    int q;
    std::cin >> q;
    while (q--) {
        int type;
        std::cin >> type;
        if (type == 1) {
            int x_query;
            std::cin >> x_query;
            if (x_query >= MAX_VAL) { 
                 std::cout << 0 << "\n";
                 continue;
            }

            long long num = count_gcd[x_query];
            long long den = (pow2[N_global] - 1 + MOD) % MOD;
            
            if (den == 0) { 
                 if (num == 0) std::cout << 0 << "\n";
                 else std::cout << 0 << "\n"; 
                   } else {
                 long long inv_den = modInverse(den);
                 long long ans = (num * inv_den) % MOD;
                 std::cout << ans << "\n";
            }

        } else {
            int idx, val_new;
            std::cin >> idx >> val_new;
            --idx; 
            int val_old = a[idx];
            
            if (val_old == val_new) continue;

            update_value(val_old, -1);
            
            a[idx] = val_new; 
            
            update_value(val_new, +1);
        }
    }

    return 0;
}
