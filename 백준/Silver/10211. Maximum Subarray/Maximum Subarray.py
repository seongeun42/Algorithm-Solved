import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    nums = [*map(int, input().split())]
    dp = [0] * N
    dp[0] = nums[0]
    for i in range(1, N):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
    print(max(dp))