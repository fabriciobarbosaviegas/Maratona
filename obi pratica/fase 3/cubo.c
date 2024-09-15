#include <stdio.h>
#include <math.h>

int main(void){

    int A, B, c = 0;
    float raizQ, raizC = 0.0;

    scanf("%d", &A);
    scanf("%d", &B);
    for(int i = A; i <= B; i++){

        raizQ = pow(i, 0.5);
        raizC = pow(i, 1/3);

        printf("%.2f\n", raizC);

    }

}