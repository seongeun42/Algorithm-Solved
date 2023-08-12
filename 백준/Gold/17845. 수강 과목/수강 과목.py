import sys
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    dp = [0] * (N + 1)
    for _ in range(K):
        i, t = map(int, input().split())
        for w in range(N, t - 1, -1):
            dp[w] = max(dp[w], i + dp[w - t])
    print(dp[N])

solve()