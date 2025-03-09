import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur):
    global cnt
    visited[cur] = cnt
    for nxt in G[cur]:
        if not visited[nxt]:
            cnt += 1
            dfs(nxt)

N, M, R = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in range(N + 1):
    G[i].sort(reverse=True)
visited = [0] * (N + 1)
cnt = 1
dfs(R)
print(*visited[1:], sep="\n")