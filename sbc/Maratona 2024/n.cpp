#include <bits/stdc++.h>
using namespace std;

#define MAX_N 50005
#define MAX_M 100005
#define MAX_K 50005
#define INF 1000000000

int n, m, k, u, v, t, t_total, adj[MAX_N][2], dist[MAX_N];
bool vis[MAX_N];
vector<pair<int, int>> edges;

int bellman_ford(int source) {
    fill(dist, dist + n + 1, INF);
    dist[source] = 0;

    for (int i = 1; i < n; i++) {
        for (auto &e : edges) {
            int u = e.first, v = e.second, w = adj[u][1];
            if (dist[u] != INF && dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
            }
        }
    }

    for (auto &e : edges) {
        int u = e.first, v = e.second, w = adj[u][1];
        if (dist[u] != INF && dist[v] > dist[u] + w) {
            return -1;
        }
    }

    return dist[n];
}

void add_edge(int u, int v, int w) {
    edges.push_back({u, v});
    adj[u][0]++;
    adj[v][1] = max(adj[v][1], w);
}

void remove_edge(int u, int v) {
    auto it = find(edges.begin(), edges.end(), make_pair(u, v));
    if (it != edges.end()) {
        edges.erase(it);
    }
    adj[u][0]--;
}

int main() {
    int t;
    scanf("%d", &t);

    for (int tc = 1; tc <= t; tc++) {
        scanf("%d %d %d", &n, &m, &k);

        for (int i = 1; i <= n; i++) {
            adj[i][0] = adj[i][1] = 0;
        }
        edges.clear();

        for (int i = 0; i < m; i++) {
            scanf("%d %d %d", &u, &v, &t);
            add_edge(u, v, t);
        }

        t_total = 0;
        for (int i = 1; i <= n; i++) {
            if (adj[i][0] == 0) continue;
            memcpy(vis, adj[i], sizeof(adj[i]));
            int ans = bellman_ford(i);
            if (ans == -1) {
                printf("-1\n");
                continue;
            }
            t_total += ans;
        }

        for (int i = 0; i < m; i++) {
            scanf("%d %d %d", &u, &v, &t);
            remove_edge(u, v);
            t_total -= adj[u][1];
            adj[u][1] = 0;
            int ans = bellman_ford(u);
            if (ans == -1) {
                printf("-1\n");
                continue;
            }
            t_total += ans;
        }

        if (t_total % k != 0) {
            printf("-1\n");
        } else {
            printf("%d\n", t_total / k);
        }
    }

    return 0;
}