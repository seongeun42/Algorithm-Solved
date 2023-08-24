import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    memory = [*map(int, input().split())]
    cost = [*map(int, input().split())]
    dp = [0] * 10001
    ans = 10001
    for i in range(N):
        am = memory[i]
        ac = cost[i]
        for c in range(10000, ac - 1, -1):
            if dp[c] < am + dp[c - ac]:
                dp[c] = am + dp[c - ac]
            if dp[c] >= M and c < ans:
                ans = c
    print(ans)

solve()   