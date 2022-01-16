n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
  mv = 1e9
  j = 1
  while j**2 <= i:
    mv = min(mv, dp[i - j**2])
    j += 1
  dp[i] = mv + 1
print(dp[n])