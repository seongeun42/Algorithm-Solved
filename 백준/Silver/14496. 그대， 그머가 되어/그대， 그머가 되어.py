from _collections import deque
import sys
input = sys.stdin.readline

def bfs(node, dest):
    q = deque([node])
    visit[node] = 1
    while q:
        node = q.popleft()
        if node == dest:
            return visit[node] - 1
        for nn in G[node]:
            if not visit[nn]:
                visit[nn] = visit[node] + 1
                q.append(nn)
    return -1

a, b = map(int, input().split())
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)
visit = [0] * (N + 1)
print(bfs(a, b))