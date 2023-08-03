import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wv = [[0, 0]] + [[*map(int, input().split())] for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]
for b in range(1, N + 1):
    for w in range(1, K + 1):
        if wv[b][0] > w:
            dp[b][w] = dp[b - 1][w]
        else:
            dp[b][w] = max(dp[b - 1][w], wv[b][1] + dp[b - 1][w - wv[b][0]])
print(dp[N][K])