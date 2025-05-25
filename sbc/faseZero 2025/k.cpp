#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int n, k;
    std::cin >> n >> k;
    std::vector<int> a(n);
    std::vector<int> b(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        std::cin >> b[i];
    }

    std::priority_queue<std::pair<long long, int>> pq;
    
    for (int i = 0; i < n; ++i) {
        pq.push({(long long)b[i], i});
    }

    std::vector<long long> result_sums;

    int count = 0;
    while (!pq.empty() && count < k) {
        std::pair<long long, int> top = pq.top();
        pq.pop();
        long long current_sum = top.first;
        int last_idx = top.second;

        result_sums.push_back(current_sum);
        count++;

        if (count == k) break; 

        for (int next_idx = last_idx + 1; next_idx < n; ++next_idx) {
            if (a[next_idx] > a[last_idx]) {
                pq.push({current_sum + b[next_idx], next_idx});
            }
        }
    }

    for (int i = 0; i < k; ++i) {
        if (i < result_sums.size()) {
            std::cout << result_sums[i] << (i == k - 1 ? "" : " ");
        } else {
            std::cout << -1 << (i == k - 1 ? "" : " ");
        }
    }
    std::cout << std::endl;

    return 0;
}
