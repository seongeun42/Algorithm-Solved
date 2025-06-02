n = int(input())
dp = [False] * 1001
dp[1], dp[3], dp[4] = True, True, True
for i in range(5, n + 1):
    if not (dp[i - 1] == dp[i - 3] == dp[i - 4] == True):
        dp[i] = True
print("SK" if dp[n] else "CY")