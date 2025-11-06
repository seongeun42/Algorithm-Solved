w, h = map(int, input().split())
# 동O, 동X, 북O, 북X (현재 방향 + 전환 가능 여부)
dp = [[[0, 0, 0, 0] for _ in range(w)] for _ in range(h)]
# 가장 윗줄(→동), 윗줄(↓북) 초기화
for i in range(1, w):
    dp[0][i] = [1, 0, 0, 0]
for i in range(1, h):
    dp[i][0] = [0, 0, 1, 0]
# print(*dp, sep="\n")
for i in range(1, h):
    for j in range(1, w):
        # 동O
        dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
        # 동X
        dp[i][j][1] = dp[i][j - 1][2]
        # 북O
        dp[i][j][2] = dp[i - 1][j][2] + dp[i - 1][j][3]
        # 북X
        dp[i][j][3] = dp[i - 1][j][0]
print(sum(dp[h - 1][w - 1]) % 100000)