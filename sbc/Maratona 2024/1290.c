#include <stdio.h>
#define MAX_CASES 1500

int encontraCaixa(int search, int* estoque, int N){
    int volume = 51, volumeI, aux;
    
    for(int i = 0; i < N; i++){
        if(search <= estoque[i]){
            aux = search - estoque[i];
            if (aux < volume){
                volume = aux;
                volumeI = i;
            }
        }

        if(volume == 0)
            break;
    }

    if(volume == 51){
        return -1;
    }

    estoque[volumeI] = -1;

    return volume;
}

int main(){
    int N, M, x, y, z, i, output[MAX_CASES], c = 0;

    while(1){
        scanf("%d %d", &N, &M);

        if(N == 0){
            break;
        }

        int pedido[N], estoque[M];

        for(i = 0; i < N; i++){
            scanf("%d %d %d", &x, &y, &z);
            pedido[i] = x*y*z;
        }

        for(i = 0; i < M; i++){
            scanf("%d %d %d", &x, &y, &z);
            estoque[i] = x*y*z;
        }

        for(i = 0; i < N; i++){
            int aux = encontraCaixa(pedido[i], estoque, M);
            if(aux == -1){
                output[c] = -1;
                break;
            }
        }

        c++;
    }

    for(i = 0; i < c; i++){
        printf("%d\n", output[i]);
    }
    return 0;
}