N = int(input())
A = [*map(int, input().split())]
dp = [0] * N
min_v = A[0]
for i in range(1, N):
    if A[i] < min_v:
        min_v = A[i]
    dp[i] = max(dp[i - 1], A[i] - min_v)
print(*dp)