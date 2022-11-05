n = int(input())
dp = [1, 2]
for i in range(2, n):
    dp.append(dp[i - 2] + dp[i - 1])
print(dp[-1] * 2 + dp[-2] * 2 if n != 1 else 4)