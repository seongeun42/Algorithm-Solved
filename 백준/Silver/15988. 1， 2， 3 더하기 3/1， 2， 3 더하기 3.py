import sys
input = sys.stdin.readline

T = int(input())
dp = [0, 1, 2, 4]
for _ in range(T):
    n = int(input())
    while len(dp) <= n:
        i = len(dp)
        dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009)
    print(dp[n])