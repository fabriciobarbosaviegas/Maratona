#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

// Definição de um trecho do rio
typedef struct {
    int u, v; // cidades conectadas
    int c;    // horas após o início do ano em que o trecho se torna trafegável
} TrechoRio;

// Estrutura para representar um nó na fila do BFS
typedef struct {
    int cidade; // cidade atual
    int tempo;  // tempo atual
} Node;

// Função de BFS para determinar o menor tempo necessário para visitar K cidades
int bfs(int n, int m, int k, TrechoRio trechos[], int cidadeInicial) {
    // Vetor para armazenar a menor quantidade de tempo necessária para visitar k cidades
    int menorTempo[k + 1];
    for (int i = 0; i <= k; ++i) {
        menorTempo[i] = INT_MAX;
    }

    // Fila para BFS
    Node fila[n * (k + 1)];
    int frente = 0, tras = 0;

    // Inicializa a BFS com a cidade inicial
    fila[tras++] = (Node){cidadeInicial, 0};

    // Marca a cidade inicial com tempo 0
    menorTempo[1] = 0;

    while (frente < tras) {
        Node atual = fila[frente++];
        int cidadeAtual = atual.cidade;
        int tempoAtual = atual.tempo;

        // Verifica se já visitamos k cidades
        int numCidadesVisitadas = 0;
        for (int i = 1; i <= n; ++i) {
            if (menorTempo[i] <= tempoAtual) {
                numCidadesVisitadas++;
            }
        }
        if (numCidadesVisitadas >= k) {
            menorTempo[k] = menorTempo[k] < tempoAtual ? menorTempo[k] : tempoAtual;
            continue;
        }

        // Itera sobre todos os trechos do rio
        for (int i = 0; i < m; ++i) {
            int u = trechos[i].u;
            int v = trechos[i].v;
            int c = trechos[i].c;

            // Verifica se o trecho do rio é trafegável no tempo atual
            if (c <= tempoAtual) {
                int proximaCidade = (cidadeAtual == u) ? v : u;
                int proximoTempo = tempoAtual + c;

                // Se o próximo tempo for menor que o menor tempo conhecido para visitar k cidades
                if (menorTempo[numCidadesVisitadas + 1] > proximoTempo) {
                    menorTempo[numCidadesVisitadas + 1] = proximoTempo;
                    fila[tras++] = (Node){proximaCidade, proximoTempo};
                }
            }
        }
    }

    // Retorna o menor tempo necessário para visitar k cidades
    return menorTempo[k];
}

// Função principal
int main() {
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);

    // Lê os trechos do rio
    TrechoRio trechos[m];
    for (int i = 0; i < m; ++i) {
        scanf("%d %d %d", &trechos[i].u, &trechos[i].v, &trechos[i].c);
    }

    // Define a cidade inicial como 1
    int cidadeInicial = 1;

    // Chama a função BFS para encontrar o menor tempo necessário para visitar k cidades
    int menorTempo = bfs(n, m, k, trechos, cidadeInicial);

    // Imprime o menor tempo encontrado
    printf("%d\n", menorTempo);

    return 0;
}