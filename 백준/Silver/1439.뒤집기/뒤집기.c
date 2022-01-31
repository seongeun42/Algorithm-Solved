#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main(){
     int i, flag=1;
     char *arr; 
     arr= (char*)malloc(sizeof(char)*1000000);
     scanf("%s", arr); 
     int zerocnt=0, onecnt =0 ; 
     if(arr[0]=='1'){
         onecnt++ ; 
         for(i =1; i<strlen(arr); i++){
              if(arr[i-1]== arr[i])continue; 
              else{
                   flag =(!flag) ;
                   if(flag==1)onecnt++ ; 
                   if(flag!=1)zerocnt++ ; 
              }
         }
         
         
     }
     if(arr[0]=='0'){
         zerocnt++ ; flag= 0 ;
         for(i =1; i<strlen(arr); i++){
              if(arr[i-1]==arr[i])continue; 
              else{
                   flag=(!flag) ;
                   if(flag ==1)onecnt++ ; 
                   if(flag!=1)zerocnt++; 
              }
         } 
     } 
    if(onecnt<zerocnt)printf("%d", onecnt); 
    else{
         printf("%d", zerocnt) ;
    }
}