import sys
input = sys.stdin.readline

def dfs(dep, p):
    if dep == 4:
        return 1
    visited[p] = 1
    for v in G[p]:
        if not visited[v]:
            if dfs(dep + 1, v):
                return 1
    visited[p] = 0
    return 0

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    p1, p2 = map(int, input().split())
    G[p1].append(p2)
    G[p2].append(p1)
visited = [0] * N
ans = 0
for i in range(N):
    if G[i]:
        if dfs(0, i):
            ans = 1
            break
print(ans)