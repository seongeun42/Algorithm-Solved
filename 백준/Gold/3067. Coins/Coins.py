import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = [*map(int, input().split())]
    M = int(input())
    dp = [0] * (M + 1)
    for c in coins:
        if c > M:
            break
        dp[c] += 1
        for i in range(c + 1, M + 1):
            dp[i] += dp[i - c]
    print(dp[M])