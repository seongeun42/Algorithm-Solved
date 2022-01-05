from collections import deque

def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for v in graph[node]:
        if not visited[v]:
            dfs(graph, v, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = False
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for k in graph[v]:
            if visited[k]:
                queue.append(k)
                visited[k] = False

n, m, v = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
for k in edge:
    graph[k[0]].append(k[1])
    graph[k[1]].append(k[0])
graph = list(map(sorted, graph))
visited = [False] * (n + 1)

dfs(graph, v, visited)
print()
bfs(graph, v, visited)