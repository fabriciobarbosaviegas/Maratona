#include <iostream>
#include <vector>
#include <string>
#include <algorithm> 

using namespace std;

struct EdgeInfo {
    int to;
    char label;
};

vector<vector<EdgeInfo>> adj;
int max_overall_periodicity = 0;

int calculate_periodicity_from_lps_val(int n, int last_lps_val) {
    if (n == 0) {
        return 0;
    }
    int len_border = last_lps_val;

    if (len_border > 0 && n % (n - len_border) == 0) {
        int p = n - len_border;
        int num_repetitions = n / p;
        if (num_repetitions >= 2) {
            return p;
        }
    }
    return 0;
}

void dfs(int u, string& current_s, vector<int>& current_lps_values) {
    if (!current_s.empty()) {
        int p = calculate_periodicity_from_lps_val(current_s.length(), current_lps_values.back());
        max_overall_periodicity = max(max_overall_periodicity, p);
    }

    for (const auto& edge : adj[u]) {
        char char_to_add = edge.label;
        current_s.push_back(char_to_add);

        int new_lps_val;
        if (current_s.length() == 1) {
            new_lps_val = 0;
        } else {
            int j = current_lps_values.back(); 
            
            while (j > 0 && char_to_add != current_s[j]) {
                j = current_lps_values[j - 1];
            }
            if (char_to_add == current_s[j]) {
                j++;
            }
            new_lps_val = j;
        }
        current_lps_values.push_back(new_lps_val);

        dfs(edge.to, current_s, current_lps_values);

        current_lps_values.pop_back();
        current_s.pop_back();
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    adj.resize(n + 1);

    if (n < 2) { 
        cout << 0 << endl;
        return 0;
    }

    vector<int> parents(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        cin >> parents[i];
    }

    string labels_str;
    cin >> labels_str;

    for (int i = 0; i < n - 1; ++i) {
        int parent_node = parents[i];
        int child_node = i + 2; 
        char label = labels_str[i];
        adj[parent_node].push_back({child_node, label});
    }

    string initial_s = "";
    vector<int> initial_lps_values; 

    dfs(1, initial_s, initial_lps_values);

    cout << max_overall_periodicity << endl;

    return 0;
}