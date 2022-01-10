def dfs(node, graph, visited, cnt):
  visited[node] = 1
  cnt[0] += 1
  for v in graph[node]:
    if not visited[v]:
      dfs(v, graph, visited, cnt)

n = int(input())
e = int(input())
edge = [list(map(int, input().split())) for _ in range(e)]
graph = [[] for _ in range(n + 1)]
for k in edge:
  graph[k[0]].append(k[1])
  graph[k[1]].append(k[0])
visited = [0] * (n + 1)
cnt = [-1]
dfs(1, graph, visited, cnt)
print(cnt[0])