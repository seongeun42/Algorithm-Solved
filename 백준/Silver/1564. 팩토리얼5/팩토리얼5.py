N = int(input())
dp = [1, 1]
for i in range(2, N + 1):
    dp.append((dp[i - 1] * i) % int(1e13))
    while dp[i] % 10 == 0:
        dp[i] //= 10
print(str(dp[N])[-5:])