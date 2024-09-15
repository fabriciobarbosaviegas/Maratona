#include <stdio.h>

int main(void){
    int anos, meses, dias, idade;
    scanf("%d", &anos);
    scanf("%d", &meses);
    scanf("%d", &dias);

    idade = (meses*12)+(dias*365)+anos;

    printf("%d", idade);
}
