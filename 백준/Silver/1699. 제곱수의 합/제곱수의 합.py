n = int(input())
sqrt = [0, 1]
dp = [0, 1, 2, 3]
for i in range(4, n + 1):
    dp.append(n)
    if (i ** 0.5) % 1 == 0:
        dp[i] = 1
        sqrt.append(i)
        continue
    for j in range(len(sqrt) - 1, 0, -1):
        if dp[i] == 2:
            break
        if dp[i] > dp[i - sqrt[j]] + dp[sqrt[j]]:
            dp[i] = dp[i - sqrt[j]] + dp[sqrt[j]]
print(dp[n])