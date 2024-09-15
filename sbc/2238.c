#include <stdio.h>

int main(){
    int a, b, c, d, n = -1;
    
    scanf("%d %d %d %d", &a, &b, &c, &d);

    if ( a == b || c == d || c % a != 0){
        printf ("%d\n" , -1) ;
        return 0;
    }
    
    for(int i = 0; i < c; i+=a){
        if(i%a==0 && i%b!=0 && c%i==0 && d%i!=0){
            n = i;
            break;
        }
    }

    printf("%d\n", n);

    return 0;
}