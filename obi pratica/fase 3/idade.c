#include <stdio.h>

int main(void){
    int n[3];
    
    for(int i = 0; i < 3; i++){
        scanf("%d", &n[i]);
    }

    int maxN = max(n);
    int minN = min(n, maxN);
    int med = 0;

    for (int i = 0; i < 3; i++)
    {
        if(n[i] < maxN && n[i] > minN){
            med = n[i];
            break;
        }
    }
    
    if(med == 0){
        printf("%d", minN);
    }

    else{
        printf("%d", med);
    }

}

int max(int n[]){
    int maxN = 0;

    for(int i = 0; i < 3; i++){
        if(n[i] > maxN){
            maxN = n[i];
        }
    }

    return maxN;
}


int min(int n[], int maxN){
    int minN = maxN;

    for(int i = 0; i < 3; i++){
        if(n[i] < minN){
            minN = n[i];
        }
    }

    return minN;
}