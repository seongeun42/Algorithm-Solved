import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(visit, graph, node):
    visit[node] = 1
    for v in graph[node]:
        if not visit[v]:
            dfs(visit, graph, v)
    return 1

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
visit = [0] * (n + 1)
cnt = 0
for i in range(1, n + 1):
    if not visit[i]:
        cnt += dfs(visit, graph, i)
print(cnt)