import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        coins = [0] + [*map(int, input().split())]
        M = int(input())
        dp = [0] * (M + 1)
        for c in coins:
            if c > M: break
            dp[c] += 1
            for m in range(c + 1, M + 1):
                dp[m] += dp[m - c]
        print(dp[m])

solve()