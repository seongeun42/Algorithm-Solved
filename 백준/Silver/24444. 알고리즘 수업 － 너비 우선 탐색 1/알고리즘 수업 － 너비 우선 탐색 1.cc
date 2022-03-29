#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int n, m, r, cnt;
int visit[100001] = {0, };
vector<int> graph[100001];

int	main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m >> r;
  for (int i = 0; i < m; i++)
  {
    int u, v;
    cin >> u >> v;
    graph[u].push_back(v);
    graph[v].push_back(u);
  }
  
  for (int i = 1; i <= n; i++)
    sort(graph[i].begin(), graph[i].end());

  cnt = 1;
  queue<int> q;
  visit[r] = 1;
  q.push(r);
  while (!q.empty())
  {
    int n = q.front();
    q.pop();
    for (int v : graph[n])
    {
      if (!visit[v])
      {
        cnt++;
        visit[v] = cnt;
        q.push(v);
      }
    }
  }

  for (int i = 1; i <= n; i++)
    cout << visit[i] << "\n";
	return 0;
}