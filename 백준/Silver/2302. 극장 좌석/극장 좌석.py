import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
fixed = [int(input()) for _ in range(M)]
dp = [1, 1, 2]
for i in range(1, 39):
    dp.append(dp[i] + dp[i + 1])
res = 1
pre = 0
for i in range(M):
    res *= dp[fixed[i] - pre - 1]
    pre = fixed[i]
print(res * dp[N - pre])