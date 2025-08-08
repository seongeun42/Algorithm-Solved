import sys
input = sys.stdin.readline

def backtrack(cur, visit, G, N, dp):
    if visit == (1 << N) - 1:
        return 0
    if dp[cur][visit] != -1:
        return dp[cur][visit]
    dp[cur][visit] = float("inf")
    for nxt in range(N):
        if visit & (1 << nxt):
            continue
        dp[cur][visit] = min(dp[cur][visit], G[cur][nxt] + backtrack(nxt, visit | (1 << nxt), G, N, dp))
    return dp[cur][visit]

def solve():
    N, K = map(int, input().split())
    T = [[*map(int, input().split())] for _ in range(N)]
    for m in range(N):
        for i in range(N):
            for j in range(N):
                if i == j: continue
                if T[i][m] + T[m][j] < T[i][j]:
                    T[i][j] = T[i][m] + T[m][j]
    dp = [[-1] * (1 << N) for _ in range(N)]
    print(backtrack(K, 1 << K, T, N, dp))

solve()