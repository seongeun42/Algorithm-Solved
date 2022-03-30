def vol_print(last):
    for i in range(M, -1, -1):
        if last[i]:
            print(i)
            return
    print(-1)

N, S, M = map(int, input().split())
Vol = [*map(int, input().split())]
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][S] = 1
for i in range(N):
    for j in range(M + 1):
        if dp[i][j] == 1:
            if 0 <= j - Vol[i]:
                dp[i + 1][j - Vol[i]] = 1
            if j + Vol[i] <= M:
                dp[i + 1][j + Vol[i]] = 1
vol_print(dp[N])