#include <iostream>
#include <numeric> 
#include <vector>
#include <algorithm> 
#include <set>       
#include <cmath>     

long long calculate_gcd(long long a, long long b) {
    a = std::abs(a); 
    b = std::abs(b);
    while (b) {
        a %= b;
        std::swap(a, b);
    }
    return a;
}

std::vector<long long> get_distinct_prime_factors(long long n) {
    std::set<long long> factors_set;
    if (n <= 1) return {};

    long long temp_n = n;
    
    if (temp_n % 2 == 0) {
        factors_set.insert(2);
        while (temp_n % 2 == 0) {
            temp_n /= 2;
        }
    }

    for (long long d = 3; d * d <= temp_n; d += 2) {
        if (temp_n % d == 0) {
            factors_set.insert(d);
            while (temp_n % d == 0) {
                temp_n /= d;
            }
        }
    }
    if (temp_n > 1) {
        factors_set.insert(temp_n);
    }
    std::vector<long long> result(factors_set.begin(), factors_set.end());
    return result;
}


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    long long y_val, k_val;
    std::cin >> y_val >> k_val;

    long long current_x = 1;
    long long k_remaining = k_val;

    if (y_val == 1) {
        current_x += k_remaining; 
        k_remaining = 0;
    }

    while (k_remaining > 0) {
        if (current_x % y_val == 0) {
            current_x += k_remaining * y_val;
            k_remaining = 0;
            break;
        }

        long long common_divisor = calculate_gcd(current_x, y_val);
        
        long long x_norm = current_x / common_divisor;
        long long y_norm = y_val / common_divisor;

        if (y_norm == 1) { 
            current_x += k_remaining * y_val; 
            k_remaining = 0;
            break;
        }

        long long steps_to_multiple_of_y = y_norm - (x_norm % y_norm);
        
        long long steps_maintaining_g_multiplier;
        std::vector<long long> prime_factors_of_y_norm = get_distinct_prime_factors(y_norm);
        
        long long min_s = -1; 
        for (long long p : prime_factors_of_y_norm) {
            long long s_for_p = p - (x_norm % p); 
            if (min_s == -1 || s_for_p < min_s) {
                min_s = s_for_p;
            }
        }
        steps_maintaining_g_multiplier = min_s;

        long long num_steps_chunk = std::min(steps_to_multiple_of_y, steps_maintaining_g_multiplier);
        
        long long actual_steps_to_take = std::min(num_steps_chunk, k_remaining);
        
        current_x += actual_steps_to_take * common_divisor;
        k_remaining -= actual_steps_to_take;
    }

    std::cout << current_x << std::endl;

    return 0;
}
