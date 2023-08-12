def solve():
    _, K = map(int, input().split())
    C = [*map(int, input().split())]
    dp = [0] + [101] * K
    maxC = 0
    for c in C:
        for k in range(min(K, maxC + c), c - 1, -1):
            if dp[k] > dp[k - c] + 1:
                dp[k] = dp[k - c] + 1
        maxC += c
    print(-1 if dp[K] == 101 else dp[K])

solve()