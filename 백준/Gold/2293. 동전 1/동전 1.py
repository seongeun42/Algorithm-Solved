n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [1] + [0] * k
for v in coin:
    for i in range(1, k + 1):
        if i - v >= 0:
            dp[i] += dp[i - v]
print(dp[k])