import sys
input = sys.stdin.readline

def solve():
    M, N = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(M)]
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    ans = 0
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if arr[i - 1][j - 1] == 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j])
    print(ans)

solve()