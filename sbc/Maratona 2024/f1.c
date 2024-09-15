#include <stdio.h>

int fact(int n) {
    int res = 1;
    for (int i = 2; i <= n; i++) {
        res *= i;
    }
    return res;
}

int main() {
    int n;
    scanf("%d", &n);
    
    int f[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &f[i]);
    }

    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += fact(f[i]);
    }

    printf("%d\n", soma);

    return 0;
}
