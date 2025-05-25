#include <iostream>
#include <vector>
#include <algorithm>

const long long INF = 4e18; 

struct Node {
    long long min_val;
};

std::vector<long long> val_array;
std::vector<Node> tree;
int N_segtree;

void build(int node_idx, int start, int end) {
    if (start == end) {
        tree[node_idx] = {val_array[start]};
    } else {
        int mid = (start + end) / 2;
        build(2 * node_idx, start, mid);
        build(2 * node_idx + 1, mid + 1, end);
        tree[node_idx].min_val = std::min(tree[2 * node_idx].min_val, tree[2 * node_idx + 1].min_val);
    }
}

int query(int node_idx, int current_start, int current_end, int query_start, int query_end, long long threshold_val) {
    if (current_start > query_end || current_end < query_start || tree[node_idx].min_val >= threshold_val) {
        return -1; 
    }
    if (current_start == current_end) { 
        return current_start;
    }

    int mid = (current_start + current_end) / 2;
    int res_left = -1;
    if (query_start <= mid) {
         res_left = query(2 * node_idx, current_start, mid, query_start, query_end, threshold_val);
    }
   
    if (res_left != -1) {
        return res_left;
    }
    
    int res_right = -1;
    if (query_end > mid) { 
        res_right = query(2 * node_idx + 1, mid + 1, current_end, query_start, query_end, threshold_val);
    }
    return res_right;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    long long k;
    std::cin >> n >> k;

    std::vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    N_segtree = 2 * n;
    val_array.resize(N_segtree);
    for (int i = 0; i < N_segtree; ++i) {
        val_array[i] = a[i % n] - (long long)i * k;
    }

    tree.resize(4 * N_segtree);
    build(1, 0, N_segtree - 1);

    std::vector<int> b(n);
    for (int s = 0; s < n; ++s) {
        long long threshold = val_array[s]; 
        int query_range_start = s + 1;
        int query_range_end = s + n;
        
        int j_abs = query(1, 0, N_segtree - 1, query_range_start, query_range_end, threshold);
        
        b[s] = (j_abs % n) + 1;
    }

    for (int i = 0; i < n; ++i) {
        std::cout << b[i] << (i == n - 1 ? "" : " ");
    }
    std::cout << std::endl;

    return 0;
}
