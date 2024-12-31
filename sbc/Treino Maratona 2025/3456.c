#include <stdio.h>

void div(long long int n){
    int b;

    while(n >= 10){
        b = n%10;
        n = (n / 10) * 3 + b;
        printf("%lld\n", n);
    }
}

int main(){
    long long int X;
    scanf("%lld", &X);

    printf("%lld\n", X);
    div(X);

    return 0;
}