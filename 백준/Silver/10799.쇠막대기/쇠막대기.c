#include <stdio.h>

int main(void){
    int nowstick = 0 , totalstick = 0, chk = 0, idx = 0;
    char str[100001];
    scanf("%s",str);
    while(str[idx] != '\0'){
        if(chk == 0){
            if(str[idx] == '('){
                nowstick++; totalstick++; }
            else{
                nowstick--; totalstick--;
                totalstick += nowstick;
                chk = 1;
            }
        }
        else{
            if(str[idx] == '('){
                nowstick++; totalstick++; chk = 0;
            }
            else{
                nowstick--;
            }
        }
        idx++;
    }
    printf("%d",totalstick);
}