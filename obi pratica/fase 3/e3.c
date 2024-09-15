#include <stdio.h>

int main(void){
    float eleitores, brancos, nulos, validos;
    float percentBrancos, percentNulos, percentValidos;

    scanf("%f", &eleitores);
    scanf("%f", &brancos);
    scanf("%f", &nulos);
    scanf("%f", &validos);

    percentBrancos = (eleitores * (brancos/100))*100;
    percentNulos = (eleitores * (nulos/100))*100;
    percentValidos = (eleitores * (validos/100))*100;

    printf("%.2f %%\n%.2f\n%.2f", percentBrancos, percentNulos, percentValidos);

}