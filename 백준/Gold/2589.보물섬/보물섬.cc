#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
int N, M, py[4]={-1, 1, 0, 0}, ph[4]={0, 0, -1, 1}, H=0;
char A[50][50];

void bfs(int y, int h)
{
  int visit[50][50]={0};
  queue <pair<int, int>> q;
  visit[y][h]=1;
  q.push({y, h});
  while (q.empty()==0)
  {
    int hy=q.front().first;
    int hh=q.front().second;
    q.pop();
    for (int i=0; i<4; i++)
    {
      int ty=hy+py[i];
      int th=hh+ph[i];
      if (0<=ty&&ty<N&&0<=th&&th<M)
      {
        if (A[ty][th]=='L'&&visit[ty][th]==0)
        {
          q.push({ty, th});
          visit[ty][th]=visit[hy][hh]+1;
          H=max(H, visit[ty][th]);
        }
      }
    }
  }
}
int main()
{
  int i, j;
  cin.tie(0);
  cout.tie(0);
  ios::sync_with_stdio(0);
  cin>>N>>M;
  for (i=0; i<N; i++)
  {
    cin>>A[i];
  }
  for (i=0; i<N; i++)
  {
    for (j=0; j<M; j++)
    {
      if (A[i][j]=='L')
      {
        bfs(i, j);
      }
    }
  }
  cout<<H-1;
  return 0;
}