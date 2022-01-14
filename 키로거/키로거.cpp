#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin >> n;
  
  while (n--)
  {
    string s;
    cin >> s;
    list<char> L;
    list<char>::iterator cur = L.end();

    for (int i = 0; i < s.length(); i++)
    {
      if (s[i] == '<' && cur != L.begin())
        --cur;
      if (s[i] == '>' && cur != L.end())
        ++cur;
      if (s[i] == '-' && cur != L.begin())
        cur = L.erase(--cur);
      if (s[i] != '<' && s[i] != '>' && s[i] != '-')
        L.insert(cur, s[i]);
    }
    for (char c : L) cout << c;
    cout << '\n';
  }
}

