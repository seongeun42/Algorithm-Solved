import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    q = deque([s])
    visit[s] = 1
    cnt = 1
    while q:
        cn = q.popleft()
        for nn in G[cn]:
            if not visit[nn]:
                cnt += 1
                visit[nn] = cnt
                q.append(nn)

N, M, R = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
for i in range(1, N + 1):
    G[i].sort(reverse=True)
    
visit = [0] * (N + 1)
bfs(R)
print(*visit[1:], sep="\n")