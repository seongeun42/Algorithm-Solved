import sys
input = sys.stdin.readline
T, W = map(int, input().split())
dp = [[0] * (W + 1) for _ in range(T + 1)]
for i in range(1, T + 1):
    p = int(input())
    dp[i][0] = dp[i - 1][0] + 1 if p == 1 else dp[i - 1][0]
    for c in range(1, W + 1):
        if c > i: break
        if p == 1 and c % 2 == 0:
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - 1]) + 1
        elif p == 2 and c % 2 == 1:
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - 1]) + 1
        else:
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - 1])
print(max(dp[-1]))