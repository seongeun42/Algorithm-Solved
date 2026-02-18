import sys
input = sys.stdin.readline

N, M = map(int, input().split())
p = set([*map(int, input().split())])
dp = [0] * (N + 1)
for i in range(1, N + 1):
    if i not in p:
        v = dp[i - 1] + 7
        for j in range(1, 4):
            if i - j <= 0:
                break
            if i - j not in p:
                v = dp[i - j] + 2 * j
        dp[i] = v
    else:
        dp[i] = dp[i - 1]
print(dp[N])