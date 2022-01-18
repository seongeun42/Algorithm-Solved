import sys
input = sys.stdin.readline

def dfs(visited, graph, node):
    visited[node] += 1
    for v in graph[node]:
        if visited[v] == -1:
            visited[v] = visited[node]
            dfs(visited, graph, v)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [-1] * (n + 1)
dfs(visited, graph, a)
print(visited[b])