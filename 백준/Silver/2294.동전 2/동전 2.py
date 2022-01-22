n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))
dp = [0] * (k + 1)
for i in range(1, k + 1):
    l = []
    for v in coin:
        if v <= i and dp[i - v] != -1:
            l.append(dp[i - v])
    if l:
        dp[i] = min(l) + 1
    else:
        dp[i] = -1
print(dp[k])