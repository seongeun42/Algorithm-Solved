import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    dp = [0] * (N + 1)
    for _ in range(M):
        d, p = map(int, input().split())
        for day in range(N, 0, -1):
            if day >= d:
                dp[day] = max(dp[day], p + dp[day - d])
    print(max(dp))

solve()