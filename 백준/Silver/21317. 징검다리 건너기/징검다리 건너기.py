import sys
input = sys.stdin.readline

N = int(input())
energy = [[*map(int, input().split())] for _ in range(N - 1)]
K = int(input())
if N == 1:
    print(0)
elif N == 2:
    print(energy[0][0])
else:
    dp = [[0, 0] for _ in range(N)]
    dp[1] = [energy[0][0], energy[0][0]]
    v = min(dp[1][0] + energy[1][0], dp[0][0] + energy[0][1])
    dp[2] = [v, v]
    for i in range(3, N):
        dp[i][0] = min(dp[i - 1][0] + energy[i - 1][0], dp[i - 2][0] + energy[i - 2][1])
        dp[i][1] = min(dp[i - 3][0] + K, dp[i - 1][1] + energy[i - 1][0], dp[i - 2][1] + energy[i - 2][1])
    print(min(dp[-1]))