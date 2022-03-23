N, M = map(int, input().split())
dp = [[0] * (M + 1)]
dp += [[0] + [*map(int, input().split())] for _ in range(N)]
for r in range(1, N + 1):
    for c in range(1, M + 1):
        dp[r][c] += max(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
print(dp[N][M])