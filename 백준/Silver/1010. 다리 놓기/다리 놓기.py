import sys
input = sys.stdin.readline

def factorial(n, dp):
  if n in dp:
    return dp[n]
  for i in range(len(dp) - 1, n + 1):
    dp[i] = dp[i - 1] * i
  return dp[n]

t = int(input())
dp = {0: 1, 1: 1}
for _ in range(t):
  n, m = map(int, input().split())
  print(factorial(m, dp) // (factorial(m - n, dp) * factorial(n, dp)))