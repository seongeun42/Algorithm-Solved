import sys
input = sys.stdin.readline

def solve():
    C, N = map(int, input().split())
    dp = [1e9] * (C + 100)
    dp[0] = 0
    for _ in range(N):
        cost, person = map(int, input().split())
        for cw in range(person, C + 100):
            if dp[cw] > cost + dp[cw - person]:
                dp[cw] = cost + dp[cw - person]
    print(min(dp[C:]))

solve()