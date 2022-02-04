n = int(input())
a = [*map(int, input().split())]
dp = [0] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(max(dp))