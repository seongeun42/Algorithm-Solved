import sys
input = sys.stdin.readline
N = int(input())
tet = []
i, num = 1, 0
while num < N:
    num += (i * (i + 1)) // 2
    tet.append(num)
    i += 1
dp = [1e9] * (N + 1)
for i in range(1, N + 1):
    for v in tet:
        if v == i:
            dp[i] = 1
            break
        if v > i:
            break
        dp[i] = min(dp[i], 1 + dp[i - v])
print(dp[N])