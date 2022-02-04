n = int(input())
nums = [*map(int, input().split())]
dp = [nums[0]]
for i in range(n-1):
    dp.append(max(dp[i] + nums[i+1], nums[i+1]))
print(max(dp))