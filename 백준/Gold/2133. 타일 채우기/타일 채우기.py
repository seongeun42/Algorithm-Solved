N = int(input())
if N % 2:
    print(0)
else:
    dp = [1] + [0] * N
    dp[2] = 3
    for i in range(4, N + 1, 2):
        dp[i] = dp[i - 2] * dp[2]
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2
    print(dp[N])