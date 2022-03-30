N = int(input())
A = [*map(int, input().split())]
dp = [0] * N
for i in range(0, N):
    for j in range(0, i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(max(dp))