from _collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([1])
    visited[1] = 1
    while q:
        nd = q.popleft()
        for v in graph[nd]:
            if not visited[v]:
                visited[v] = nd
                q.append(v)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
visited = [0] * (n + 1)
bfs()
print(*visited[2:], sep='\n')