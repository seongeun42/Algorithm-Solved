from collections import deque
import sys
input = sys.stdin.readline

def bfs(node, visited):
    q = deque([node])
    visited[node-1] = 1
    cnt = 1
    while q:
        v = q.popleft()
        for n in graph[v]:
            if not visited[n-1]:
                cnt += 1
                visited[n-1] = 1
                q.append(n)
    return cnt

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    c1, c2 = map(int, input().split())
    graph[c2].append(c1)
res = [[] for _ in range(N+1)]
for i in range(1, N+1):
    visited = [0] * N
    res[bfs(i, visited)].append(i)
for r in res[::-1]:
    if r:
        print(*sorted(r), sep=' ')
        break