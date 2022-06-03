#include <bits/stdc++.h>
using namespace std;

int n;
int res = 0;
int q[15] = {0,};

bool check(int r)
{
  for (int i = 0; i < r; i++)
    if (q[i] == q[r] || abs(q[r] - q[i]) == r - i )
      return false;
  return true;
}

void qeens(int r)
{
  if (r == n)
  {
    res++;
    return;
  }

  for (int i = 0; i < n; i++)
  {
    q[r] = i;
    if (check(r))
      qeens(r + 1);
  }
}

int main()
{
  cin >> n;
  qeens(0);
  cout << res;
}

