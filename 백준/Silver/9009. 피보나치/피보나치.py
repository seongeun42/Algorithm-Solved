import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    dp = [0, 1]
    for i in range(2, 45):
        dp.append(dp[i - 2] + dp[i - 1])
    for _ in range(T):
        n = int(input())
        ans = []
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] <= n:
                n -= dp[i]
                ans.append(dp[i])
            if n == 0:
                break
        print(*ans[::-1])

solve()