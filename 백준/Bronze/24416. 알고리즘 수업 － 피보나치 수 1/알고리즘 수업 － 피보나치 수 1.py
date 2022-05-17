n = int(input())
c2 = n - 2 if n > 1 else 1
dp = [0, 1, 1]
for i in range(3, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])
print(dp[n], c2)