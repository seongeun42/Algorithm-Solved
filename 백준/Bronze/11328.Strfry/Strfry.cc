#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string alpha ="abcdefghijklmnopqrstuvwxyz";
    
    int N;
    cin>>N;
    
    for(int i=0;i<N;i++){
        string str1,str2;
        int arr1[26]={0,};
        int arr2[26]={0,};
        
        cin>>str1>>str2;
        if(str1.length()!=str2.length()){
            cout<<"Impossible"<<'\n';
            continue;
        }
        else {
            for(int j=0;j<str1.length();j++){
                for(int l=0;l<26;l++){
                    if(str1[j]==alpha[l]) arr1[l]++;
                    if(str2[j]==alpha[l]) arr2[l]++;
                }
            }
        }
        for(int q=0;q<26;q++){
            if(arr1[q]!=arr2[q]){
                cout<<"Impossible"<<'\n';
                break;
            }
            else{
                if(q==25){
                    cout<<"Possible"<<'\n';
                }
            }
        }
    }
}
