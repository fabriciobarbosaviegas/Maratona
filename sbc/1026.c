#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void transformaEmBinario(long long int decimal, long long int bin[32]);
void somaBinariaDeMofiz(long long int binA[32], long long int binB[32], long long int soma[32]);
long long int binarioParaInteiro(long long int bin[32]);

int main(){
    long long int a, b, aBin[32], bBin[32], somaBin[32], *soma = NULL, somaLen = 0;
    
    while(scanf("%lld %lld", &a, &b) != EOF){
        transformaEmBinario(a, aBin);
        transformaEmBinario(b, bBin);
        somaBinariaDeMofiz(aBin, bBin, somaBin);

        somaLen++;
        soma = realloc(soma, somaLen*sizeof(long long int));
        if(soma == NULL){
            return 1;
        }

        soma[somaLen-1] = binarioParaInteiro(somaBin);
   }

    for(long long int i = 0; i < somaLen; i++){
        printf("%lld\n", soma[i]);
    }
    free(soma);

    return 0;
}

void transformaEmBinario(long long int decimal, long long int bin[32]){
    for(long long int i = 31; i >= 0; i--){
        if(decimal > 0){
            if(decimal % 2 == 0){
                bin[i] = 0;
            }
            else{
                bin[i] = 1;
            }
            decimal /= 2;
        }
        else{
            bin[i] = 0;
        }
    }
    return;
}

void somaBinariaDeMofiz(long long int binA[32], long long int binB[32], long long int soma[32]){
    for(long long int i = 0; i < 32; i++){
        if(binA[i] + binB[i] > 1){
            soma[i] = 0;
        }
        else{
            soma[i] = binA[i] + binB[i];
        }
    }
    return;
}

long long int binarioParaInteiro(long long int bin[32]){
    long long int soma = 0;
    for(long long int i = 31; i >= 0; i--){
        if(bin[i] != 0){
            soma += pow(2, (32-(i+1)));
        }
    }
    return soma;
}