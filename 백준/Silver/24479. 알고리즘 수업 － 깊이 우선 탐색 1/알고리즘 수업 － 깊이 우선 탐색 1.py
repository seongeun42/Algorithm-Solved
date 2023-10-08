import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

cnt = 1

def dfs(node, ans, G):
    global cnt
    ans[node] = cnt
    cnt += 1
    for nn in G[node]:
        if not ans[nn]:
            dfs(nn, ans, G)

def solve():
    N, M, R = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    for i in range(N + 1):
        G[i].sort()
    ans = [0] * (N + 1)
    dfs(R, ans, G)
    print(*ans[1:], sep="\n")

solve()