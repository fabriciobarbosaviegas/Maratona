#include <stdio.h>
#include <stdlib.h>

// Função de comparação para o heap máximo
int compare(const void *a, const void *b) {
    return (*(int *)b - *(int *)a);
}

int min_stops(int N, int K, int A[], int B[]) {
    int current_tobacco = K;
    int stops = 0;
    int idx = 0;
    int heap_size = 0;
    int *max_heap = (int *)malloc(N * sizeof(int));

    while (idx < N) {
        // Adicionar lojas ao heap até não poder mais avançar
        while (idx < N && current_tobacco >= A[idx]) {
            max_heap[heap_size++] = B[idx];
            qsort(max_heap, heap_size, sizeof(int), compare); // Ordena o heap
            idx++;
        }

        // Verificar se o Saci já chegou na última loja
        if (idx == N) {
            free(max_heap);
            return stops;
        }

        // Se o Saci não pode alcançar a próxima loja e não há mais tabaco disponível
        if (heap_size == 0) {
            free(max_heap);
            return -1;
        }

        // Pegue o máximo de tabaco disponível nas lojas passadas
        current_tobacco += max_heap[0];
        max_heap[0] = max_heap[--heap_size];
        qsort(max_heap, heap_size, sizeof(int), compare); // Ordena o heap
        stops++;
    }

    // Se restar distância a percorrer após a última loja
    while (current_tobacco < A[N-1]) {
        if (heap_size == 0) {
            free(max_heap);
            return -1;
        }
        current_tobacco += max_heap[0];
        max_heap[0] = max_heap[--heap_size];
        qsort(max_heap, heap_size, sizeof(int), compare); // Ordena o heap
        stops++;
    }

    free(max_heap);
    return stops;
}

int main() {
    int N, K;
    scanf("%d %d", &N, &K);
    int *A = (int *)malloc(N * sizeof(int));
    int *B = (int *)malloc(N * sizeof(int));

    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }

    for (int i = 0; i < N; i++) {
        scanf("%d", &B[i]);
    }

    int result = min_stops(N, K, A, B);
    printf("%d\n", result);

    free(A);
    free(B);
    return 0;
}