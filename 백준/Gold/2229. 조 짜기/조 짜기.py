N = int(input())
score = [*map(int, input().split())]
dp = [0] * N
for i in range(1, N):
    min_v, max_v = score[i], score[i]
    for j in range(i - 1, -1, -1):
        if max_v < score[j]:
            max_v = score[j]
        if min_v > score[j]:
            min_v = score[j]
        hap = max_v - min_v
        if j > 0:
            hap += dp[j - 1]
        if dp[i] < hap:
            dp[i] = hap
print(dp[-1])