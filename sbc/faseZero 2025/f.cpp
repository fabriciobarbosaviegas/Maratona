#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <limits>
const int SUM_OFFSET = 2000;
const int MAX_SUM_VAL = 2000;
const int MIN_SUM_VAL = -2000; 
const int SUM_ARRAY_SIZE = MAX_SUM_VAL - MIN_SUM_VAL + 1;


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    std::vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    std::vector<std::vector<std::pair<int, int>>> sum_pairs_map(SUM_ARRAY_SIZE);

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int current_sum = a[i] + a[j];
            if (current_sum >= MIN_SUM_VAL && current_sum <= MAX_SUM_VAL) {
                sum_pairs_map[current_sum + SUM_OFFSET].push_back({i, j});
            }
        }
    }

    for (int i = 0; i < SUM_ARRAY_SIZE; ++i) {
        if (!sum_pairs_map[i].empty()) {
            std::sort(sum_pairs_map[i].begin(), sum_pairs_map[i].end());
        }
    }

    int q_count;
    std::cin >> q_count;

    for (int k_query = 0; k_query < q_count; ++k_query) {
        int target_q;
        std::cin >> target_q;

        long long quadruplet_count = 0;

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int sum_ij = a[i] + a[j];
                int remaining_sum_kl = target_q - sum_ij;

                if (remaining_sum_kl >= MIN_SUM_VAL && remaining_sum_kl <= MAX_SUM_VAL) {
                    const auto& candidates_kl = sum_pairs_map[remaining_sum_kl + SUM_OFFSET];
                    if (!candidates_kl.empty()) {
                        auto it = std::upper_bound(candidates_kl.begin(), candidates_kl.end(), 
                                                   std::make_pair(j, std::numeric_limits<int>::max()));
                        
                        quadruplet_count += std::distance(it, candidates_kl.end());
                    }
                }
            }
        }
        std::cout << quadruplet_count << "\n";
    }

    return 0;
}
