#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, p=0; cin>>n;
    for(int i=0; i<n; i++)
    {
        string a; stack<char>b;
        short A=0, B=0; cin>>a; b.push('C');
        for(int j=0; j<a.length(); j++)
        {
            if(a[j]=='A')
            {
                if(a[j]==b.top()){A--; b.pop();}
                else{A++; b.push(a[j]);}
            }
            if(a[j]=='B')
            {
                if(a[j]==b.top()){B--; b.pop();}
                else{B++; b.push(a[j]);}
            }
        }
        if(b.size()==1) p++;
        while(b.size()!=0) b.pop();
    }cout<<p<<endl;

    return 0;
}