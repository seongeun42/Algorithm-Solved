N = int(input())
nums = [int(input()) for _ in range(N)]
dp = [0] * N
for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[j], dp[i])
    dp[i] += 1
print(N - max(dp))