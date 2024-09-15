#include <stdio.h>
#include <stdlib.h>

int main(){
    long long int a, b, *somas = NULL, somasLen = 0;
    
    while(scanf("%lld %lld", &a, &b) != EOF){
        somasLen++;
        somas = realloc(somas, somasLen*sizeof(long long int));
        somas[somasLen-1] = a^b;
    }

    for(int i = 0; i < somasLen; i++){
        printf("%lld\n",somas[i]);
    }

    free(somas);
    return 0;
}