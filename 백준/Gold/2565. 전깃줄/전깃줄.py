N = int(input())
AB = sorted([[*map(int, input().split())] for _ in range(N)])
dp = [0] * N
for i in range(N):
    for j in range(i):
        if AB[i][1] > AB[j][1]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(N - max(dp))