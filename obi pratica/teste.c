#include <stdio.h>
#include <stdlib.h>

int main() {
    unsigned int num1, num2;
    unsigned int *output = NULL; // Vetor dinâmico para armazenar a saída
    int output_size = 0; // Tamanho atual do vetor
    int eof_detected = 0;

    while (!eof_detected) {
        int scan_result = scanf("%u %u", &num1, &num2);
        
        if (scan_result == EOF) {
            eof_detected = 1;
        } else {
            unsigned int sum = num1 ^ num2; // Realiza a soma sem considerar o carry
            unsigned int carry = (num1 & num2) << 1; // Calcula o carry
            
            while (carry != 0) {
                unsigned int temp = sum;
                sum = sum ^ carry; // Realiza a soma bit a bit
                carry = (temp & carry) << 1; // Atualiza o carry
            }

            // Aloca mais um elemento no vetor
            output_size++;
            output = realloc(output, output_size * sizeof(unsigned int));
            if (output == NULL) {
                printf("Erro ao alocar memória.\n");
                return 1; // Saída com erro
            }

            // Armazena o resultado no vetor
            output[output_size - 1] = sum;
        }
    }

    // Imprime a saída
    for (int i = 0; i < output_size; i++) {
        printf("%u\n", output[i]);
    }

    // Libera a memória alocada para o vetor
    free(output);
    
    return 0;
}
