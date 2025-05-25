#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* intToBinary(int n, int num_bits) {
    char* binaryString = (char*)malloc(num_bits + 1);
    if (binaryString == NULL) {
        exit(EXIT_FAILURE);
    }
    for (int i = num_bits - 1; i >= 0; i--) {
        binaryString[num_bits - 1 - i] = ((n >> i) & 1) ? '1' : '0';
    }
    binaryString[num_bits] = '\0';
    return binaryString;
}

int isPalindrome(char* str) {
    int l = 0;
    int h = strlen(str) - 1;
    while (h > l) {
        if (str[l++] != str[h--]) {
            return 0; 
        }
    }
    return 1; 
}

int main() {
    int x;
    scanf("%d", &x);

    for (int y = x; y >= 1; y--) {
        int num_bits = 0;
        if (y == 0) {
            num_bits = 1;
        } else {
            int temp = y;
            while(temp > 0){
                temp >>= 1;
                num_bits++;
            }
        }
        if (num_bits == 0) num_bits = 1; 

        char* binary_y = intToBinary(y, num_bits);
        if (isPalindrome(binary_y)) {
            printf("%d\n", y);
            free(binary_y);
            break;
        }
        free(binary_y);
    }

    return 0;
}