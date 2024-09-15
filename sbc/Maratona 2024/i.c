#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Função para verificar se o colar é especial
bool is_special_necklace(char *necklace_str, int L, int M) {
    // Convertendo a string para um vetor de inteiros
    int necklace[L];
    for (int i = 0; i < L; i++) {
        necklace[i] = necklace_str[i] - '0';
    }

    // Verificando todas as rotações do colar
    for (int rotation = 0; rotation < L; rotation++) {
        bool seen_counts[L + 1]; // Array para armazenar os contadores de contas pretas vistas
        memset(seen_counts, false, sizeof(seen_counts));

        bool is_special = true;

        // Verificando todos os blocos de tamanho M
        for (int start = 0; start < L; start += M) {
            int black_count = 0;

            // Contando contas pretas no bloco atual
            for (int i = 0; i < M; i++) {
                black_count += necklace[(rotation + start + i) % L];
            }

            // Verificando se este número de contas pretas já foi visto
            if (seen_counts[black_count]) {
                is_special = false;
                break;
            }
            seen_counts[black_count] = true;
        }

        // Se o colar for especial, retornamos true
        if (is_special) {
            return true;
        }
    }

    // Se nenhuma rotação resultou em um colar especial, retornamos false
    return false;
}

// Função principal
int main() {
    char necklace_1[] = "10000111111101";
    int M_1 = 2;
    int L_1 = strlen(necklace_1);
    if (is_special_necklace(necklace_1, L_1, M_1)) {
        printf("True\n"); // Deve retornar True
    } else {
        printf("False\n");
    }

    char necklace_2[] = "1000100110001";
    int M_2 = 2;
    int L_2 = strlen(necklace_2);
    if (is_special_necklace(necklace_2, L_2, M_2)) {
        printf("True\n");
    } else {
        printf("False\n"); // Deve retornar False
    }

    return 0;
}
