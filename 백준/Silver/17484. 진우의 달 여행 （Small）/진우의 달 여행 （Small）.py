import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(N)]
    dp = [[[1e9] * 3 for _ in range(M)] for _ in range(N)]
    for i in range(M):
        dp[0][i] = [arr[0][i]] * 3
    for i in range(1, N):
        for j in range(M):
            if j < M - 1:
                dp[i][j][0] = arr[i][j] + min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2])
            dp[i][j][1] = arr[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])
            if j > 0:
                dp[i][j][2] = arr[i][j] + min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1])
    print(min(map(min, dp[-1])))

solve()