import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(cur, flag):
    visit[cur] = flag
    for nxt in G[cur]:
        if not visit[nxt]:
            if dfs(nxt, -flag) == 0:
                return 0
        elif visit[nxt] == flag:
            return 0
    return 1

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visit = [0] * (N + 1)
ans = 1
for i in range(1, N + 1):
    if not visit[i]:
        if dfs(i, 1) == 0:
            ans = 0
            break
print(ans)