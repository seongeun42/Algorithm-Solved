import sys
input = sys.stdin.readline

def solve():
    N, M, H = map(int, input().split())
    dp = [1] + [0] * H
    for _ in range(N):
        B = [*map(int, input().split())]
        tmp = dp[:]
        for b in B:
            for h in range(b, H + 1):
                dp[h] += tmp[h - b]
    print(dp[H] % 10007)

solve()