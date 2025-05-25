#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int N_nodes;
std::vector<int> target_counts_global(6);
std::vector<std::vector<bool>> vertex_allowed_values_global;
std::vector<std::vector<int>> adj_global;
int P_special_paths;
std::vector<std::vector<int>> parsed_special_paths_global;
std::vector<std::vector<std::pair<int, int>>> node_on_path_data_global;

std::vector<int> current_assignment_global;
std::vector<int> current_counts_remaining_global(6);

std::vector<int> get_path_bfs(int start_node, int end_node) {
    std::vector<int> q_bfs; 
    std::vector<int> parent(N_nodes + 1, 0);
    std::vector<bool> visited(N_nodes + 1, false);

    if (start_node < 1 || start_node > N_nodes || end_node < 1 || end_node > N_nodes) {
        return {}; 
    }
    
    q_bfs.push_back(start_node);
    visited[start_node] = true;
    
    int head = 0;
    bool found = false;
    while(head < q_bfs.size()){
        int u = q_bfs[head++];
        if (u == end_node) {
            found = true;
            break;
        }
        for (int v : adj_global[u]) {
            if (!visited[v]) {
                visited[v] = true;
                parent[v] = u;
                q_bfs.push_back(v);
            }
        }
    }

    std::vector<int> path;
    if (!found) {
        return path; 
    }

    int curr = end_node;
    while (true) {
        path.push_back(curr);
        if (curr == start_node) break;
        if (parent[curr] == 0 && curr != start_node) return {}; 
        curr = parent[curr];
        if (path.size() > N_nodes) return {}; 
    }
    std::reverse(path.begin(), path.end());
    return path;
}

bool backtrack_recursive(int vertex_idx) {
    if (vertex_idx == N_nodes + 1) {
        return true; 
    }

    for (int val = 1; val <= 5; ++val) {
        if (vertex_allowed_values_global[vertex_idx][val]) {
            if (current_counts_remaining_global[val] > 0) {
                current_assignment_global[vertex_idx] = val;
                current_counts_remaining_global[val]--;

                bool possible = true;
                for (const auto& path_info : node_on_path_data_global[vertex_idx]) {
                    int path_id = path_info.first;
                    int pos_in_path = path_info.second; 
                    const auto& current_path_nodes = parsed_special_paths_global[path_id];

                    if (pos_in_path > 0) { 
                        int prev_node = current_path_nodes[pos_in_path - 1];
                        if (current_assignment_global[prev_node] != 0) {
                            if (current_assignment_global[prev_node] >= val) {
                                possible = false;
                            }
                        }
                    }
                    if (!possible) break;

                    if (pos_in_path < current_path_nodes.size() - 1) {
                        int next_node = current_path_nodes[pos_in_path + 1];
                        if (current_assignment_global[next_node] != 0) {
                            if (val >= current_assignment_global[next_node]) {
                                possible = false;
                            }
                        }
                    }
                    if (!possible) break; 
                }

                if (possible) {
                    if (backtrack_recursive(vertex_idx + 1)) {
                        return true;
                    }
                }

                current_counts_remaining_global[val]++;
                current_assignment_global[vertex_idx] = 0;
            }
        }
    }
    return false;
}


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::cin >> N_nodes;

    adj_global.resize(N_nodes + 1);
    vertex_allowed_values_global.resize(N_nodes + 1, std::vector<bool>(6, false));
    node_on_path_data_global.resize(N_nodes + 1);
    current_assignment_global.resize(N_nodes + 1, 0);

    for (int i = 1; i <= 5; ++i) {
        std::cin >> target_counts_global[i];
    }
    current_counts_remaining_global = target_counts_global;

    for (int i = 1; i <= N_nodes; ++i) {
        int M_allowed;
        std::cin >> M_allowed;
        for (int j = 0; j < M_allowed; ++j) {
            int allowed_val;
            std::cin >> allowed_val;
            if (allowed_val >=1 && allowed_val <=5)
                vertex_allowed_values_global[i][allowed_val] = true;
        }
    }

    for (int i = 0; i < N_nodes - 1; ++i) {
        int u, v;
        std::cin >> u >> v;
        adj_global[u].push_back(v);
        adj_global[v].push_back(u);
    }

    std::cin >> P_special_paths;
    parsed_special_paths_global.resize(P_special_paths);

    for (int i = 0; i < P_special_paths; ++i) {
        int path_start_node, path_end_node;
        std::cin >> path_start_node >> path_end_node;
        
        parsed_special_paths_global[i] = get_path_bfs(path_start_node, path_end_node);
        
        if (parsed_special_paths_global[i].empty() && N_nodes > 0) { 
             std::cout << -1 << std::endl; 
             return 0;
        }

        if (parsed_special_paths_global[i].size() > 5) {
            std::cout << -1 << std::endl;
            return 0;
        }

        for (size_t j = 0; j < parsed_special_paths_global[i].size(); ++j) {
            int node_on_p = parsed_special_paths_global[i][j];
            node_on_path_data_global[node_on_p].push_back({i, static_cast<int>(j)});
        }
    }
    
    if (backtrack_recursive(1)) {
        for (int i = 1; i <= N_nodes; ++i) {
            std::cout << current_assignment_global[i] << (i == N_nodes ? "" : " ");
        }
        std::cout << std::endl;
    } else {
        std::cout << -1 << std::endl;
    }

    return 0;
}
