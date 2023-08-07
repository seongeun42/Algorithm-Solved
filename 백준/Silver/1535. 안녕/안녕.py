def solve():
    N = int(input())
    hp = [0] + [*map(int, input().split())]
    plea = [0] + [*map(int, input().split())]
    dp = [0] * 100
    for i in range(1, N + 1):
        w, v = hp[i], plea[i]
        for pw in range(99, 0, -1):
            if pw >= w:
                dp[pw] = max(dp[pw], v + dp[pw - w])
    print(dp[99])

solve()