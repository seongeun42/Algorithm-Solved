import sys
input = sys.stdin.readline

def solve():
    while 1:
        N = int(input())
        if N == 0:
            break
        P = [int(input()) for _ in range(N)]
        dp = [0] * N
        dp[0] = P[0]
        for i in range(1, N):
            dp[i] = max(dp[i - 1] + P[i], P[i])
        print(max(dp))

solve()