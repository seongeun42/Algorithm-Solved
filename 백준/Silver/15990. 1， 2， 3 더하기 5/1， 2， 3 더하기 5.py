import sys
input = sys.stdin.readline

dp = [(), (1, 0, 0), (0, 1, 0), (1, 1, 1)]

T = int(input())
for _ in range(T):
    n = int(input())
    if n >= len(dp):
        while len(dp) <= n:
            one = (dp[len(dp) - 1][1] + dp[len(dp) - 1][2]) % 1000000009
            two = (dp[len(dp) - 2][0] + dp[len(dp) - 2][2]) % 1000000009
            three = (dp[len(dp) - 3][0] + dp[len(dp) - 3][1]) % 1000000009
            dp.append((one, two, three))
    print(sum(dp[n]) % 1000000009)