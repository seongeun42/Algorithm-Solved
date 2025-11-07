import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    TP = [[*map(int, input().split())] for _ in range(N)]
    dp = [0 for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        t, p = TP[i]
        end = i + t
        if end <= N and dp[i + 1] < p + dp[end]:
            dp[i] = p + dp[end]
        else:
            dp[i] = dp[i + 1]
    print(dp[0])

solve()