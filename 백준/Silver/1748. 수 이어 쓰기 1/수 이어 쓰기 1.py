n = int(input())
dp = [0, 9] + [9 * (10 ** i) * (i + 1) for i in range(1, 9)] + [1]
d = len(str(n))
print((n - (10 ** (d - 1)) + 1) * d + sum(dp[0:d]))