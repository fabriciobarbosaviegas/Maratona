#include <stdio.h>
#include <stdlib.h>

#define MAX 5001

int parent[MAX];
int rank[MAX];

void swap(int* a, int* b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

void make_set(int v) {
    parent[v] = v;
    rank[v] = 0;
}

int find_set(int v) {
    if (v == parent[v])
        return v;
    return parent[v] = find_set(parent[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (rank[a] < rank[b])
            swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b])
            rank[a]++;
    }
}

int main() {
    int N, M, D;
    scanf("%d %d %d", &N, &M, &D);

    for (int i = 1; i <= N; i++)
        make_set(i);

    for (int i = 0; i < M; i++) {
        int U, V;
        scanf("%d %d", &U, &V);
        union_sets(U, V);
    }

    int count = 0;
    for (int i = 1; i <= N; i++) {
        if (find_set(i) == i)
            count++;
    }

    int houses = count;
    int roads = count - 1;

    printf("%d %d\n", houses, roads);

    return 0;
}