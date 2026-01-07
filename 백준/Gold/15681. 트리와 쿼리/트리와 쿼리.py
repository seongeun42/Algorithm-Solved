import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur, tree, dp, visited):
    for nxt in tree[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, tree, dp, visited)
            dp[cur] += dp[nxt]

def solve():
    N, R, Q = map(int, input().split())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    dp = [1] * (N + 1)
    visited = [False] * (N + 1)
    visited[R] = True
    dfs(R, tree, dp, visited)
    for _ in range(Q):
        print(dp[int(input())])

solve()