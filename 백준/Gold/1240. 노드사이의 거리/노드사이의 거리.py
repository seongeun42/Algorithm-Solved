import sys
input = sys.stdin.readline

def dfs(node, dist, end):
    global flag
    visit[node] = dist
    if node == end:
        flag = 1
        return
    for n, w in G[node]:
        if not visit[n]:
            dfs(n, dist + w, end)
        if flag: return

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2, w = map(int, input().split())
    G[n1].append((n2, w))
    G[n2].append((n1, w))

for _ in range(M):
    visit = [0] * (N + 1)
    s, e = map(int, input().split())
    flag = 0
    dfs(s, 1, e)
    print(visit[e] - 1)