#include <stdio.h>
#include <stdlib.h>

#define MAX_N 101

int pai[MAX_N];
int rank[MAX_N];

void init(int n) {
    for (int i = 1; i <= n; i++) {
        pai[i] = i;
        rank[i] = 0;
    }
}

int find(int x) {
    if (pai[x] != x) {
        pai[x] = find(pai[x]);
    }
    return pai[x];
}

void union_set(int x, int y) {
    int root_x = find(x);
    int root_y = find(y);

    if (root_x != root_y) {
        if (rank[root_x] < rank[root_y]) {
            pai[root_x] = root_y;
        } else if (rank[root_x] > rank[root_y]) {
            pai[root_y] = root_x;
        } else {
            pai[root_y] = root_x;
            rank[root_x]++;
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);

    init(n);

    for (int i = 1; i <= n + 1; i++) {
        int m;
        scanf("%d", &m);

        for (int j = 0; j < m; j++) {
            int u, v;
            scanf("%d %d", &u, &v);

            union_set(u, v);
        }
    }

    int grupos[MAX_N] = {0};
    for (int i = 1; i <= n; i++) {
        int root = find(i);
        grupos[root]++;
    }

    int t = 0;
    for (int i = 1; i <= n; i++) {
        if (grupos[i] > 0) {
            t++;
        }
    }

    printf("%d\n", t);

    for (int i = n; i >= 1; i--) {
        if (grupos[i] > 0) {
            printf("%d ", grupos[i]);
        }
    }
    printf("\n");

    return 0;
}