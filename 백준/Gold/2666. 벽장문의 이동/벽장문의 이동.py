import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    o1, o2 = sorted(map(int, input().split()))
    T = int(input())
    dp = [[[1e9] * (N + 1) for _ in range(N + 1)] for _ in range(T + 1)]
    dp[0][o1][o2] = 0
    for i in range(T):
        target = int(input())
        for l in range(1, N):
            for r in range(l + 1, N + 1):
                if dp[i][l][r] == 1e9:
                    continue
                if target < r:
                    dp[i + 1][target][r] = min(dp[i + 1][target][r], dp[i][l][r] + abs(l - target))
                if target > l:
                    dp[i + 1][l][target] = min(dp[i + 1][l][target], dp[i][l][r] + abs(target - r))
    print(min(map(min, dp[-1])))

solve()