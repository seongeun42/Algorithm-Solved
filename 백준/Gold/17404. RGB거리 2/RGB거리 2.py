import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    cost = [[*map(int, input().split())] for _ in range(N)]
    R, G, B = 0, 1, 2
    ans = 1e9
    for color in range(3):
        dp = [[1e9, 1e9, 1e9] for _ in range(N)]
        dp[0][color] = cost[0][color]
        for i in range(1, N):
            dp[i][R] = cost[i][R] + min(dp[i - 1][G], dp[i - 1][B])
            dp[i][G] = cost[i][G] + min(dp[i - 1][R], dp[i - 1][B])
            dp[i][B] = cost[i][B] + min(dp[i - 1][R], dp[i - 1][G])
        for i in range(3):
            if i != color and ans > dp[-1][i]:
                ans = dp[-1][i]
    print(ans)

solve()