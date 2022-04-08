N = int(input())
A = [*map(int, input().split())]
dp = [[0] * 21 for _ in range(N - 1)]
dp[0][A[0]] = 1
for i in range(N - 2):
    for j in range(21):
        if dp[i][j] > 0:
            if j + A[i + 1] <= 20:
                dp[i + 1][j + A[i + 1]] += dp[i][j]
            if 0 <= j - A[i + 1]:
                dp[i + 1][j - A[i + 1]] += dp[i][j]
print(dp[-1][A[-1]])