#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
    int times = n*2-1;
    int printTimes = times;
    int end = n;
    
    for(int i = (times/2)+0.5+1; i > 0; i--){
        printReverseRange(n, end-1);
        printRange(end, n+1);
        printf("\n");
        end--;
    }

    end++;
    for(int i = (times/2)+0.5; i > 0; i--){
        end++;
        printReverseRange(n, end-1);
        printf("\n");
    }
    
    //printReverseRange(n, 0);
    return 0;
}


int printRange(int init, int end){

    for(int i = init; i < end; i++){
        printf("%d ", i);
    }
    
    return 0;
    
}

int printReverseRange(int init, int end){

    for(int i = init; i > end; i--){
        printf("%d ", i);
    }
    
    return 0;
    
}
int printNTimes(char str, int times){
    for(int i = 0; i < times; i++){
        printf("%s ", str);
    }
    
    return 0;
}
