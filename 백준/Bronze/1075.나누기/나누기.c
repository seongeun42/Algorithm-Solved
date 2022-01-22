//1075 나누기
#include <stdio.h>

int main(){
    
    int N, F;
    
    scanf("%d %d", &N, &F);
    
    for(N -= N % 100; N % F; N++);
    
    printf("%02d", N % 100);
        
    return 0;
}