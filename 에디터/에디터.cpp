#include <bits/stdc++.h>
using namespace std;

int main()
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  string s;
  int n;
  cin >> s;
  cin >> n;
  list<char> L;
  for (char c : s) L.push_back(c);
  list<char>::iterator cur = L.end();

  while (n--)
  {
    char op;
    cin >> op;
    if (op == 'L' && cur != L.begin())
      --cur;
    if (op == 'D' && cur != L.end())
      ++cur;
    if (op == 'B' && cur != L.begin())
    {
      --cur;
      cur = L.erase(cur);
    }
    if (op == 'P')
    {
      char c;
      cin >> c;
      L.insert(cur, c);
    }
  }
  for (char c : L) cout << c;
}