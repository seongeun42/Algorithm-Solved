import sys
input = sys.stdin.readline

N = int(input())
P = [0] + [*map(int, input().split())]
dp = P[:]
for i in range(1, N + 1):
    dp[i] = min([dp[i - j] + dp[j] for j in range(i // 2 + 1)])
print(dp[N])